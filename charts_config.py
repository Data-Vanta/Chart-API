# charts_config.py

# --- Knowledge Base (all chart definitions here) ---

charts_config = [
    {
        "name": "bar_chart",
        "title": "Bar Chart",
        "why": [
            "To compare categories quickly and clearly",
            "To show counts, sums, or averages of different groups",
            "Easy to read and widely understood"
        ],
        "use_cases": [
            "Business: Compare sales across different products or regions",
            "Education: Show student counts per class or grades per subject",
            "Marketing: Compare performance of campaigns or channels",
            "Finance: Display revenue or expenses across departments",
            "Survey results: Visualize responses per category"
        ],
        "data_requirements": {
            "x_axis": "Categories (discrete values)",
            "y_axis": "Numerical values (counts, sums, averages)"
        }
    },
    {
        "name": "heatmap",
        "title": "Heatmap",
        "why": [
            "To highlight patterns and relationships quickly through colors",
            "To make large sets of values easier to compare visually",
            "To detect hidden correlations or areas of high/low intensity"
        ],
        "use_cases": [
            "Correlation matrix",
            "User behavior patterns",
            "Gene expression",
            "Stock/index performance",
            "Student grades across subjects"
        ],
        "data_requirements": {
            "x_axis": "Categories or continuous values",
            "y_axis": "Categories or continuous values",
            "values": "Numerical values represented by color intensity"
        }
    },
    {
        "name": "bubble_chart",
        "title": "Bubble Chart",
        "why": [
            "To visualize relationships among three or more variables",
            "To compare entities by position and size",
            "To make data storytelling engaging",
            "To display correlation and trends"
        ],
        "use_cases": [
            "Investment analysis",
            "Research visualizations",
            "Marketing analytics",
            "Healthcare comparisons"
        ],
        "data_requirements": {
            "x_axis": "Numeric",
            "y_axis": "Numeric",
            "bubble_size": "Numeric",
            "optional": "Categories for bubble colors"
        }
    },
    {
        "name": "pivot_table",
        "title": "Pivot Table",
        "why": [
            "To analyze large datasets fast",
            "To slice and dice data",
            "To avoid writing manual formulas"
        ],
        "use_cases": [
            "Sales totals",
            "Expense analysis",
            "Customer segmentation",
            "HR stats",
            "Survey analytics"
        ],
        "data_requirements": {
            "rows": "Categories to group by",
            "columns": "Optional cross-tab categories",
            "values": "Numerical fields to aggregate",
            "aggregation": "sum | count | avg | min | max"
        }
    }
]

# --- Derived sets your API needs ---

minimal_config = [
    {
        "name": chart["name"],
        "why": chart["why"],
        "use_cases": chart["use_cases"]
    }
    for chart in charts_config
]

chart_requirements = {
    chart["name"]: chart.get("data_requirements", {})
    for chart in charts_config
}
