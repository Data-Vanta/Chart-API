import uvicorn
import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import AsyncOpenAI
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from charts_config import charts_config, minimal_config, chart_requirements

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
    description="An API that suggests charts based on user prompts and maps data schemas to them.",
    version="1.0.0"
)


# --- Pydantic Models for API Validation ---

# Models for /choose-charts
class ChooseChartRequest(BaseModel):
    user_prompt: str

class ChartChoice(BaseModel):
    name: str

class ChooseChartResponse(BaseModel):
    chosen_charts: List[ChartChoice]

# Models for /map-schema
class MapSchemaRequest(BaseModel):
    user_prompt: str
    chosen_charts: List[ChartChoice]
    schema_definition: Dict[str, Any] # e.g., {"columns": {"Region": "string", "Sales": "number"}}

class MappedChartStructure(BaseModel):
    # This is highly dynamic, so we allow extra fields
    class Config:
        extra = 'allow'

class MappedChart(BaseModel):
    name: str
    structure: Dict[str, Any] # Using Dict[str, Any] for flexibility

class MapSchemaResponse(BaseModel):
    charts: List[MappedChart]


# --- Core Logic Functions 
async def choose_chart_logic(user_prompt: str, model: str = MODEL) -> str:
    """Calls OpenAI API to choose charts based on a user prompt."""
    system_prompt = """
      You are a data visualization assistant.
      You are given a list of chart configurations (with name, why, and use_cases).
      Your task is:
      1. Read the user request carefully.
      2. Compare it with the provided chart configurations.
      3. You must choose ALL charts that are relevant to the user's request, not just the most obvious one.
      4. If no chart is relevant, return {"chosen_charts": []}.
      5. Return ONLY the chosen charts as JSON in this format:

      {
        "chosen_charts": [
          {
            "name": "<chart_name>"
          }
        ]
      }

      Return JSON ONLY. No extra text, no markdown, no explanations.
      """

    try:
        response = await CLIENT.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"User request: {user_prompt}\n\nCharts config: {json.dumps(minimal_config, indent=0)}"}
            ],
            temperature=0,
        )
        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling OpenAI API: {str(e)}")

async def map_schema_to_charts_logic(user_prompt: str, chosen_charts: List[Dict], schema: Dict, model: str = MODEL) -> Dict:
    """Calls OpenAI API to map schema columns to chart requirements."""
    schema_mapping_prompt = """
    Your task:
    - For each chart, suggest the best mapping of schema columns to the chart's data requirements.
    - Use the user's request to understand what columns matter (e.g., "sales by region" → x_axis=region, y_axis=SUM(sales)).
    - Infer derived metrics from the request if needed (e.g., "profit margin" → profit/sales, "GDP per capita" → gdp/population, "average sales" → AVG(sales)).
    - Fill missing numeric axes with sensible aggregations (COUNT, SUM, AVG) if the user implicitly asks for summaries.
    - Include optional fields (color, size, labels, series) if a suitable column exists in the schema to enrich the visualization.
    - For charts with multiple metrics, suggest series as structured objects: {"name": "<metric_name>", "metric": "<column or expression>"}.
    - Handle time-based columns smartly: infer month, quarter, year, or week if the user mentions a trend.
    - Only assign schema columns that exist in the dataset.
    - If no suitable column is found for a requirement, set it to null.
    - Some charts may not need x/y axes (e.g., pie, radar, word cloud, treemap). In those cases, fill only the relevant requirements; optional fields may be added if useful.
    - Avoid generic nulls for optional enrichment fields if a categorical column exists; use the first suitable column.
    - Return ONLY JSON in this format:

    {
      "charts": [
        {
          "name": "<chart_name>",
          "structure": {
            "<requirement_1>": "<column_name, expression, or null>",
            "<requirement_2>": "<column_name, expression, or null>",
            "<requirement_3>": "<column_name, expression, or null>",
            "optional": {
              "color": "<column_name or null>",
              "size": "<column_name or null>",
              "labels": "<column_name or null>",
              "series": [{"name": "<metric_name>", "metric": "<column or expression>"}]
            }
          }
        }
      ]
    }
    """

    try:
        response = await CLIENT.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": schema_mapping_prompt},
                {"role": "user", "content": json.dumps({
                    "user_request": user_prompt,
                    "schema": schema,
                    "chosen_charts": chosen_charts,
                    "chart_requirements": chart_requirements
                }, indent=2)}
            ],
            temperature=0,
        )
        
        # Try to parse the JSON response from the LLM
        response_content = response.choices[0].message.content
        return json.loads(response_content)
        
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, 
            detail=f"OpenAI API returned non-JSON response: {response_content}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling OpenAI API: {str(e)}")

# --- API Endpoints ---

@app.get("/charts-config", summary="Get Full Chart Configuration")
async def get_charts_config():
    """
    Returns the complete `charts_config` JSON object, which includes
    names, descriptions, use cases, and data requirements for all
    supported charts.
    """
    return charts_config

@app.post("/choose-charts",
          response_model=ChooseChartResponse,
          summary="Suggest Charts from Prompt")
async def api_choose_charts(request: ChooseChartRequest):
    """
    Takes a user's natural language prompt and returns a list of
    suggested chart types that are relevant to the request.
    """
    json_string = await choose_chart_logic(request.user_prompt)
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, 
            detail=f"OpenAI API returned non-JSON response: {json_string}"
        )

@app.post("/map-schema",
          response_model=MapSchemaResponse,
          summary="Map Data Schema to Charts")
async def api_map_schema(request: MapSchemaRequest):
    """
    Takes a user prompt, a list of chosen charts, and a data schema,
    and returns a detailed mapping of schema columns to the
    data requirements for each chart.
    """
    # Convert Pydantic models back to simple dicts for the logic function
    chosen_charts_list = [chart.dict() for chart in request.chosen_charts]
    
    data = await map_schema_to_charts_logic(
        user_prompt=request.user_prompt,
        chosen_charts=chosen_charts_list,
        schema=request.schema_definition
    )
    return data

# --- Run the Application ---

if __name__ == "__main__":
    print("Starting FastAPI server...")
    print("API documentation will be available at http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)