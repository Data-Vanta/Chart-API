# ChartSense API

ChartSense is an intelligent API backend designed to bridge the gap between natural language and data visualization. It uses a Large Language Model (LLM) to:

1. **Suggest relevant chart types** based on a user's prompt (e.g., "show me sales over time").
2. **Map data schema columns** to the specific requirements of those charts (e.g., mapping `{"OrderDate": "datetime"}` to a line chart's `x_axis`).

This enables applications where users can simply describe the visualization they want.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- An OpenRouter API Key

---

## 1. Configuration (`.env`)

Create a `.env` file in the project root:

```ini
OPENROUTER_API_KEY="sk-or-your-key-here"
OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
OPENROUTER_MODEL="mistralai/mistral-7b-instruct:free"
```

### How to get your configuration

- **API Key:**  
  Create one at https://openrouter.ai/keys

- **Model:**  
  Choose one from https://openrouter.ai/models  
  Use the model’s full ID.

- **Base URL:**  
  Keep as `https://openrouter.ai/api/v1`

---

## 2. Installation & Running

### Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
python main.py
```

The API will run at: **http://127.0.0.1:8000**

---

# 📖 API Endpoints

API docs available at: **http://127.0.0.1:8000/docs**

---

## 1. `GET /charts-config`

Returns the full `charts_config.json`.

### Example Response

```json
{
  "bar_chart": {
    "name": "bar_chart",
    "description": "Displays categorical data with rectangular bars.",
    "requirements": {
      "required": ["x_axis", "y_axis"],
      "optional": ["color", "labels"]
    }
  },
  "line_chart": {
    "name": "line_chart",
    "description": "Displays data points connected by straight line segments, ideal for time-series.",
    "requirements": {
      "required": ["x_axis_time", "y_axis"],
      "optional": ["series", "color"]
    }
  }
}
```

---

## 2. `POST /choose-charts`

Suggests chart types based on natural language.

### Request Body

```json
{
  "user_prompt": "Show me monthly sales trends by region"
}
```

### Example Response

```json
{
  "chosen_charts": [
    { "name": "line_chart" }
  ]
}
```

---

## 3. `POST /map-schema`

Maps schema columns to chart requirements.

### Request Body

```json
{
  "user_prompt": "Show me monthly sales trends by region",
  "chosen_charts": [
    { "name": "line_chart" }
  ],
  "schema_definition": {
    "columns": {
      "OrderDate": "datetime",
      "Sales": "number",
      "Region": "string"
    }
  }
}
```

### Example Response

```json
{
  "charts": [
    {
      "name": "line_chart",
      "structure": {
        "x_axis_time": "OrderDate",
        "y_axis": "SUM(Sales)",
        "optional": {
          "color": "Region",
          "size": null,
          "labels": null,
          "series": [
            {
              "name": "Sales by Region",
              "metric": "Region"
            }
          ]
        }
      }
    }
  ]
}
```

---

# 🧪 Testing

1. Start the server:
   ```bash
   python main.py
   ```
2. Open **http://127.0.0.1:8000/docs**
3. Test all endpoints interactively.

---
