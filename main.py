import uvicorn
import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import AsyncOpenAI
from typing import List, Dict, Any, Union, Optional
from dotenv import load_dotenv
from charts_config import charts_config

# --- Load .env ---
load_dotenv()

# --- Configuration & API Client Setup ---
API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL")
MODEL = os.getenv("OPENROUTER_MODEL")

if not API_KEY:
    raise RuntimeError("Missing OPENROUTER_API_KEY in .env!")

CLIENT = AsyncOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Chart Generation Assistant API",
    description="An API that suggests charts and builds queries based on user prompts and metadata.",
    version="2.0.0"
)

# --- Logic Classes (Adapted from prompt2.py) ---

class ChartSuggester:
    def __init__(self, charts_config: List[Dict], model: str = MODEL):
        self.model = model
        self.minimal_config = [
            {
                "id": chart.get("chart_id"),
                "name": chart.get("name"),
                "why": chart.get("why"),
                "use_cases": chart.get("use_cases")
            }
            for chart in charts_config
        ]
        self.system_prompt = """
        You are a data visualization assistant.
        You are given a list of chart configurations (id, name, why, use_cases).
        Your task:
        1. Read the user's request carefully.
        2. Compare it with the provided chart configurations.
        3. Choose ALL charts relevant to the user's request. Do not pick just the most obvious.
        4. If no chart is relevant, return {"chosen_charts": []}.
        5. Return ONLY JSON, in this exact format:

        {
          "chosen_charts": [
            {"id": "<chart_id>", "name": "<chart_name>"}
          ]
        }

        Do not include any extra text, explanation, or markdown.
        Do not make assumptions about the dataset yet.
        """

    async def suggest(self, user_prompts: List[str]) -> List[Dict]:
        results = []

        for prompt in user_prompts:
            try:
                response = await CLIENT.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {
                            "role": "user",
                            "content": f"User request: {prompt}\nCharts config: {json.dumps(self.minimal_config, separators=(',', ':'))}"
                        }
                    ],
                    temperature=0,
                )
                content = response.choices[0].message.content
                # Handle potential JSON parsing errors or wrapping
                try:
                    chosen_charts = json.loads(content)["chosen_charts"]
                except (KeyError, json.JSONDecodeError):
                    # Fallback or empty if parsing failed
                    chosen_charts = []

                results.append({
                    "user_prompt": prompt,
                    "chosen_charts": chosen_charts
                })
            except Exception as e:
                # Log error and return empty for this prompt
                print(f"Error processing prompt '{prompt}': {e}")
                results.append({
                    "user_prompt": prompt,
                    "chosen_charts": []
                })

        return results


class ChartValidatorAndQueryBuilder:
    def __init__(self, charts_config: List[Dict], model: str = MODEL):
        self.model = model
        self.minimal_config = [
            {
                "id": chart.get("chart_id"),
                "name": chart.get("name"),
                "data_requirements": chart.get("data_requirements", {}),
            }
            for chart in charts_config
        ]
        self.system_prompt = """
        You are a data visualization assistant.

        Your task is to take the dataset metadata, recommended charts (already linked to user prompts),
        and chart configurations including data requirements.

        For each recommended chart:
        1. Check if the dataset satisfies its requirements.
        2. Identify which specific columns should be used for this chart.
        3. Skip charts that cannot be applied.

        For applicable charts, build a JSON describing the chart with:
            - user_prompt: the original user request
            - chart_id
            - chart_type (name)
            - query:
                - source: "uploaded_file"
                - select: columns with aggregation if needed
                - filters: (if any applicable from user's request)
                - group_by: (if applicable)
                - order_by: (if applicable)
                - limit: null
            - encoding: map chart axes to selected columns

        Return ONLY JSON in this format:
        {
          "intent": "visualization",
          "charts": [
            {
              "user_prompt": "<original user prompt>",
              "chart_id": "<id>",
              "chart_type": "<name>",
              "query": {
                "source": "uploaded_file",
                "select": [],
                "filters": [],
                "group_by": [],
                "order_by": [],
                "limit": null
              },
              "encoding": {"x": "", "y": "", "color": ""}
            }
          ]
        }

        Focus on dataset compatibility and fulfilling the user's request.
        Do NOT add extra text or explanations.
        """

    async def build_final_charts(self, dataset_metadata: Dict, recommended_charts_with_prompts: List[Dict]) -> Dict:
        try:
            response = await CLIENT.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {
                        "role": "user",
                        "content": f"Dataset metadata: {json.dumps(dataset_metadata)}\nRecommended charts with prompts: {json.dumps(recommended_charts_with_prompts)}\nChart configurations: {json.dumps(self.minimal_config)}"
                    }
                ],
                temperature=0,
            )
            content = response.choices[0].message.content
            return json.loads(content)
        except json.JSONDecodeError:
            return {"intent": "visualization", "charts": []}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error in Query Builder: {str(e)}")


# --- Pydantic Models ---

class SuggestChartsRequest(BaseModel):
    user_prompts: List[str]

class SuggestChartsResponse(BaseModel):
    suggestions: List[Dict[str, Any]]

class BuildQueriesRequest(BaseModel):
    dataset_metadata: Dict[str, Any]
    suggestions: List[Dict[str, Any]]

class BuildQueriesResponse(BaseModel):
    intent: str
    charts: List[Dict[str, Any]]


# --- API Endpoints ---

@app.get("/charts-config", summary="Get Full Chart Configuration")
async def get_charts_config():
    """Returns the complete charts_config JSON object."""
    return charts_config

@app.post("/suggest-charts", response_model=SuggestChartsResponse, summary="Suggest Charts from Prompts")
async def api_suggest_charts(request: SuggestChartsRequest):
    """
    Takes a list of natural language prompts and returns suggested chart types 
    relevant to each request using 'Model 1' logic.
    """
    suggester = ChartSuggester(charts_config)
    results = await suggester.suggest(request.user_prompts)
    return {"suggestions": results}

@app.post("/build-queries", response_model=BuildQueriesResponse, summary="Validate & Build Chart Queries")
async def api_build_queries(request: BuildQueriesRequest):
    """
    Takes dataset metadata and suggested charts, validates them against requirements,
    and builds the final query/encoding JSON using 'Model 2' logic.
    """
    builder = ChartValidatorAndQueryBuilder(charts_config)
    final_result = await builder.build_final_charts(request.dataset_metadata, request.suggestions)
    return final_result

# --- Run the Application ---
if __name__ == "__main__":
    print("Starting FastAPI server...")
    print("API documentation available at http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)