# charts_config.py

charts_config = [
  {
    "chart_id": 1,
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
      "Survey results: Visualize responses per category (e.g., satisfaction levels)"
    ],
    "data_requirements": {
      "x_axis": "Categories (discrete values)",
      "y_axis": "Numerical values (counts, sums, averages)"
    }
  },
  {
    "chart_id": 2,
    "name": "heatmap",
    "title": "Heatmap",
    "why": [
      "To highlight patterns and relationships quickly through colors",
      "To make large sets of values easier to compare visually",
      "To detect hidden correlations or areas of high/low intensity"
    ],
    "use_cases": [
      "Correlation matrix: Show the correlation strength between variables using colors",
      "User behavior analysis: Days of the week × hours of the day grid showing website visits (reveals peak times)",
      "Biology/genomics: Visualizing gene expression data",
      "Finance: Show stock or index performance over time using color intensity",
      "Education: Student grades across subjects, highlighting strong and weak areas"
    ],
    "data_requirements": {
      "x_axis": "Categories or continuous values (e.g., time, variables)",
      "y_axis": "Categories or continuous values (e.g., variables, groups)",
      "values": "Numerical values represented by color intensity"
    }
  },
  {
    "chart_id": 3,
    "name": "bubble_chart",
    "title": "Bubble Chart",
    "why": [
      "To visualize relationships among three or more variables at once",
      "To compare entities not only by position but also by relative size",
      "To make data storytelling more engaging and intuitive",
      "Can visually display correlation and trend"
    ],
    "use_cases": [
      "Project/Investment analysis: Compare projects across cost (X), value (Y), and risk (bubble size)",
      "Scientific research: Facilitate understanding of social, economic, medical, and other complex relationships",
      "Marketing: Show number of leads (X) vs. conversion rate (Y), with campaign budget as bubble size",
      "Healthcare: Visualize patients’ age (X) vs. treatment success rate (Y), with sample size as bubble size"
    ],
    "data_requirements": {
      "x_axis": "Numerical values (e.g., cost, leads, age)",
      "y_axis": "Numerical values (e.g., value, conversion rate, treatment success rate)",
      "bubble_size": "Numerical variable representing magnitude (e.g., risk, budget, sample size)",
      "optional": "Categories or groups can be added for bubble colors"
    }
  },
  {
    "chart_id": 4,
    "name": "histogram",
    "title": "Histogram",
    "why": [
      "To understand the shape of data distribution (normal, skewed, uniform, etc.)",
      "To detect patterns like central tendency, spread, and outliers",
      "To support decisions in statistics, such as checking normality before applying certain tests"
    ],
    "use_cases": [
      "Education: Show how student grades are distributed",
      "Business: Analyze purchase amounts or customer ages",
      "Healthcare: Visualize distribution of patients’ blood pressure readings",
      "Manufacturing: Detect variability in product dimensions",
      "Finance: Show distribution of daily returns for a stock"
    ],
    "data_requirements": {
      "x_axis": "A single numerical variable to be divided into bins",
      "y_axis": "Frequency or count of values within each bin",
      "optional": "Can include categories or groups to compare multiple distributions"
    }
  },
  {
    "chart_id": 5,
    "name": "scatter_plot",
    "title": "Scatter Plot",
    "why": [
      "To visualize relationships or correlations between two variables",
      "To identify patterns, clusters, or outliers in data",
      "To determine whether variables have a positive, negative, or no correlation"
    ],
    "use_cases": [
      "Business: Analyze relationship between advertising spend (X) and sales revenue (Y)",
      "Health: Compare exercise hours (X) with weight loss (Y)",
      "Education: Study the relation between study time (X) and exam score (Y)",
      "Science: Show how temperature (X) impacts crop yield (Y)"
    ],
    "data_requirements": {
      "x_axis": "Numerical values (independent variable, e.g., spend, hours, study time, temperature)",
      "y_axis": "Numerical values (dependent variable, e.g., revenue, weight loss, exam score, yield)",
      "optional": "Categories or groups can be added for color coding; point size can represent a third numerical variable"
    }
  },
  {
    "chart_id": 6,
    "name": "pie_chart",
    "title": "Pie Chart",
    "why": [
      "To visualize proportions in a dataset",
      "To make it easy to see which category is the largest or smallest",
      "Useful for simple comparisons when the number of categories is small"
    ],
    "use_cases": [
      "Business: Show market share of competitors or revenue distribution by product line",
      "Finance: Display expense breakdown or budget allocation",
      "Marketing: Visualize customer segments or campaign source contributions",
      "Healthcare: Show distribution of diseases or patient categories",
      "Education/Research: Present survey results or exam grade distributions"
    ],
    "data_requirements": {
      "categories": "Categorical variable representing different groups or segments",
      "values": "Numerical values corresponding to the size of each category (e.g., counts, percentages, revenue)",
      "optional": "Labels for clarity; limited to a small number of categories for readability"
    }
  },
  {
    "chart_id": 7,
    "name": "calendar_heatmap",
    "title": "Calendar Heatmap",
    "why": [
      "To visualize trends over time in a calendar layout",
      "To quickly spot daily, weekly, monthly, or seasonal patterns",
      "To make time-based data more engaging and easier to interpret"
    ],
    "use_cases": [
      "GitHub activity: Show commits per day across months/years",
      "Website analytics: Track visits or user activity by day",
      "Health/Fitness: Visualize steps taken, calories burned, or hours slept per day",
      "Sales/Operations: Display daily sales volume or tickets resolved over a year",
      "Education: Monitor student attendance or study hours per day"
    ],
    "data_requirements": {
      "date": "Date values (daily granularity, e.g., YYYY-MM-DD)",
      "value": "Numerical value for each date (e.g., commits, visits, steps, sales)",
      "optional": "Color scale to represent intensity; can include categories for multiple users/groups"
    }
  },
  {
  "chart_id": 8,
  "name": "box_plot",
  "title": "Box Plot",
  "why": [
    "Useful for visualizing the spread and variability of a numeric variable.",
    "Helps compare distributions between multiple groups effectively.",
    "Great for detecting outliers, skewness, and distribution shape.",
    "Not suitable when the dataset contains no numeric columns or when the numeric column has too few values to compute quartiles."
  ],
  "use_cases": [
    "Business: Compare monthly sales distributions across regions.",
    "Education: Show test score distributions for different classes.",
    "Healthcare: Compare recovery times between treatments.",
    "Finance: Analyze stock return distributions across companies.",
    "Manufacturing: Detect variability in product quality between batches."
  ],
  "data_requirements": {
    "must_have": {
      "numeric_column": "A continuous numeric column is required to plot the distribution (e.g., charges, revenue, test scores, durations)."
    },
    "optional": {
      "category_column": "A categorical column may be included to compare distributions between groups (e.g., contract type, gender, region)."
    },
    "not_supported": [
      "Using a binary yes/no column as the numeric variable.",
      "Generating box plots when there is no numeric variable at all.",
      "Categorical-only comparisons with no numeric measure."
    ]
  }
},
  {
    "chart_id": 9,
    "name": "line_chart",
    "title": "Line Chart",
    "why": [
      "To visualize trends and patterns over time",
      "To highlight increases, decreases, and fluctuations in data",
      "To easily compare multiple series by plotting multiple lines"
    ],
    "use_cases": [
      "Finance: Track stock prices or revenue growth over months/years",
      "Marketing: Show website visits, ad clicks, or conversions over time",
      "Healthcare: Monitor patient vitals (e.g., heart rate, blood pressure) across time",
      "Education: Track student performance or attendance trends",
      "Weather/Environment: Display temperature, rainfall, or pollution levels over days/weeks"
    ],
    "data_requirements": {
      "x_axis": "Time variable (e.g., days, months, years, timestamps)",
      "y_axis": "Numerical values representing the metric being tracked (e.g., stock price, visits, vitals)",
      "optional": "Multiple series can be included for comparison; categories or groups for color-coded lines"
    }
  },
  {
    "chart_id": 10,
    "name": "big_number",
    "title": "Big Number",
    "why": [
      "To highlight the most important metric at a glance",
      "To help stakeholders quickly understand performance without digging into details",
      "Useful for dashboards where decision-makers need instant insights"
    ],
    "use_cases": [
      "Business Metrics: Display total sales today, monthly revenue, or profit margin",
      "Marketing: Show number of new signups, daily active users, or website visitors",
      "Finance: Present current stock price, ROI, or account balance",
      "Operations: Track orders fulfilled, tickets resolved, or uptime percentage",
      "Healthcare: Display patient count, average wait time, or critical alerts"
    ],
    "data_requirements": {
      "value": "A single numerical metric to highlight (e.g., sales, signups, stock price)",
      "optional": "Comparison value (e.g., vs. previous day/week/month); label or unit for context"
    }
  },
  {
  "chart_id": 11,
  "name": "paired_t_test_table",
  "title": "Paired T-Test Table",
  "why": [
    "To determine whether there is a statistically significant difference between two related samples",
    "To analyze changes over time within the same group",
    "To check if an intervention, treatment, or condition had a real effect"
  ],
  "use_cases": [
    "Medical studies: Compare patients’ blood pressure before and after taking a drug",
    "Education: Compare students’ test scores before and after a training program",
    "Business/Marketing: Compare sales performance before and after a campaign",
    "Manufacturing/Engineering: Measure product quality before and after a process change"
  ],
  "data_requirements": {
    "sample_1": "First set of related measurements (e.g., before values)",
    "sample_2": "Second set of related measurements (e.g., after values)",
    "requirement": "Data must be paired (same subjects measured twice)"
  }
},
  {
  "chart_id": 12,
  "name": "horizon_chart",
  "title": "Horizon Chart",
  "why": [
    "To visualize large time-series datasets in a compact way",
    "To compare multiple time-series side by side without taking too much space",
    "To highlight trends, peaks, and dips clearly with color intensity"
  ],
  "use_cases": [
    "Finance: Show stock price movements across many companies in one dashboard",
    "Web analytics: Compare website traffic patterns across different pages",
    "IoT / Sensors: Visualize multiple sensor readings over time (e.g., temperature, pressure)",
    "Operations: Monitor server loads or system performance metrics",
    "Transportation: Track traffic flow patterns across multiple routes"
  ],
  "data_requirements": {
    "x_axis": "Time (continuous values, e.g., days, hours, timestamps)",
    "y_axis": "Values of the time-series",
    "series": "Multiple related time-series to compare",
    "color": "Represents intensity of change (positive or negative)"
  }
},
  {
  "chart_id": 13,
  "name": "stepped_line_chart",
  "title": "Stepped Line Chart",
  "why": [
    "To emphasize discrete changes instead of gradual trends",
    "Helps when data changes only at specific points (not continuously)",
    "Makes it easy to spot plateaus and sudden shifts in data"
  ],
  "use_cases": [
    "Subscriptions / Users: Number of subscribers stays the same until a batch of new signups or cancellations",
    "Inventory: Stock levels remain constant, then drop when sales happen",
    "Finance: Interest rates, which change step by step, not gradually",
    "Utilities: Electricity pricing tiers, where cost per unit jumps after thresholds",
    "Project Tracking: Milestones completion over time"
  ],
  "data_requirements": {
    "x_axis": "Time or ordered categories",
    "y_axis": "Values that change in steps (counts, levels, rates)",
    "series": "One or multiple discrete data series"
  }
},
  {
  "chart_id": 14,
  "name": "smooth_line_chart",
  "title": "Smooth Line Chart",
  "why": [
    "To show trends over time in a more fluid and natural way",
    "To reduce the jagged look of a normal line chart, making patterns easier to see",
    "Often used when the exact point values are less important than the overall trend"
  ],
  "use_cases": [
    "Finance: Show smooth trends in stock prices or revenue without distracting sharp fluctuations",
    "Marketing: Visualize long-term growth in website traffic or customer signups",
    "Healthcare: Track smooth trends in patient vitals or health metrics",
    "Environment: Display gradual climate changes, like average yearly temperatures",
    "Presentations: When communicating data to a non-technical audience, smooth lines make the chart easier to interpret"
  ],
  "data_requirements": {
    "x_axis": "Time or ordered categories",
    "y_axis": "Continuous numerical values",
    "series": "One or multiple data series, smoothed using interpolation or curve fitting"
  }
},
  {
  "chart_id": 15,
  "name": "waterfall_chart",
  "title": "Waterfall Chart",
  "why": [
    "To break down a total into its components of increase and decrease",
    "Makes it easy to see how individual factors contribute to the final outcome"
  ],
  "use_cases": [
    "Finance & Accounting: Revenue → Expenses → Taxes → Net Profit",
    "Sales Analysis: Starting sales, regional contributions, discounts, churn, ending sales",
    "Project Management: Planned cost → overruns → savings → final cost",
    "Performance Analysis: How different factors impact a KPI (e.g., profit margin, ROI)"
  ],
  "data_requirements": {
    "categories": "Ordered stages or components contributing to the total",
    "values": "Numerical values representing increases, decreases, and totals",
    "start_end": "A clear starting value and ending value to show the breakdown"
  }
  },
  {
  "chart_id": 16,
  "name": "area_chart",
  "title": "Area Chart",
  "why": [
    "To visualize trends and changes over time",
    "To emphasize the magnitude of values by filling the area",
    "To compare multiple categories using stacked areas"
  ],
  "use_cases": [
    "Finance: Show revenue growth or stock price changes over months/years",
    "Web analytics: Display website visits, signups, or user activity trends",
    "Marketing: Track ad impressions or campaign reach over time",
    "Healthcare: Monitor patient counts or hospital admissions over days/weeks",
    "Environmental data: Show temperature, rainfall, or pollution trends over time"
  ],
  "data_requirements": {
    "x_axis": "Time or ordered categories",
    "y_axis": "Continuous numerical values",
    "series": "One or multiple data series (can be stacked to show contribution of each series)"
  }
},
  {
  "chart_id": 17,
  "name": "big_number_with_trendline",
  "title": "Big Number with Trendline",
  "why": [
    "To highlight a key metric (e.g., total revenue, active users, sales today)",
    "To add context by showing how that metric has evolved historically",
    "To give both a snapshot + trend in one visualization"
  ],
  "use_cases": [
    "Business Dashboards: Display total sales with a monthly trend",
    "Web Analytics: Show number of active users + growth trend",
    "Finance: Show profit/loss with trend over last quarters",
    "Healthcare: Show patients served + trendline of visits"
  ],
  "data_requirements": {
    "metric": "A single key number or KPI",
    "time_series": "Historical data to show the trendline (optional but recommended)",
    "x_axis": "Time (for the trendline)",
    "y_axis": "Values associated with the key metric over time"
  }
},
{
  "chart_id": 18,
  "name": "funnel_chart",
  "title": "Funnel Chart",
  "why": [
    "To track conversion rates or drop-offs between steps in a process",
    "Helps identify bottlenecks where most users/customers drop off",
    "Easy way to visualize how many items/people remain after each stage of a sequential process"
  ],
  "use_cases": [
    "Sales Funnel: From leads → opportunities → negotiations → closed deals",
    "Marketing Funnel: Visitors → signups → trial users → paid customers",
    "Recruitment Funnel: Applicants → shortlisted → interviewed → hired",
    "Customer Journey: Awareness → consideration → purchase → loyalty",
    "Process Analysis: Any step-by-step process where numbers shrink at each stage"
  ],
  "data_requirements": {
    "stages": "Ordered stages in the process (categories)",
    "values": "Numerical values showing count or percentage at each stage",
    "conversion": "Optional calculation of conversion/drop-off rates between stages"
  }
},
  {
  "chart_id": 19,
  "name": "sunburst_chart",
  "title": "Sunburst Chart",
  "why": [
    "To visualize hierarchical relationships in data",
    "Makes it easy to see how categories are broken down into subcategories",
    "Helps compare proportions at multiple levels at once"
  ],
  "use_cases": [
    "Business: Revenue breakdown (Region → Country → Product)",
    "Website Analytics: Traffic sources (Direct → Social → Platform)",
    "Finance: Budget distribution (Department → Project → Expense)",
    "Biology: Taxonomy of species (Kingdom → Phylum → Class → Order)",
    "Organization Structures: Company hierarchy (Division → Department → Team)"
  ],
  "data_requirements": {
    "hierarchy": "Levels of categories arranged in parent → child relationships",
    "values": "Numerical values associated with each category (e.g., revenue, counts)",
    "colors": "Optional use of colors to distinguish categories or highlight groups"
  }
},
  {
  "chart_id": 20,
  "name": "tree_chart",
  "title": "Tree Chart",
  "why": [
    "To represent hierarchical relationships clearly",
    "Helps in breaking down complex structures into simple levels",
    "Makes it easy to see parent–child relationships and dependencies"
  ],
  "use_cases": [
    "Business & Management: Organizational charts (CEO → Managers → Employees)",
    "Computer Science: File system hierarchy, decision trees, data structures",
    "Project Planning: Work breakdown structures, task dependencies",
    "Biology: Family trees, species classification",
    "Education: Concept breakdowns, taxonomy of knowledge"
  ],
  "data_requirements": {
    "nodes": "Entities or items in the hierarchy",
    "links": "Parent–child relationships connecting nodes",
    "levels": "Multiple levels of hierarchy to show structure"
  }
},
  {
  "chart_id": 21,
  "name": "tree_map_chart",
  "title": "Tree Map",
  "why": [
    "To compare proportions between categories and subcategories",
    "To show hierarchical relationships while also comparing size and color metrics",
    "Useful when dealing with large datasets with multiple levels"
  ],
  "use_cases": [
    "Business & Finance: Revenue distribution (Company → Product line → Product)",
    "Stock Market: Market capitalization by sector/company",
    "File Systems: Storage usage (Folder → Subfolder → Files)",
    "Project Management: Resource allocation across projects/departments",
    "Research & Education: Topic breakdowns, taxonomy visualization"
  ],
  "data_requirements": {
    "hierarchy": "Categories and subcategories arranged in parent → child relationships",
    "size": "Numerical value represented by the area of each rectangle",
    "color": "Optional metric represented by color intensity or categories"
  }
},
  {
  "chart_id": 22,
  "name": "radar_chart",
  "title": "Radar Chart",
  "why": [
    "To visualize multivariate data in a compact, easy-to-compare format",
    "Good for identifying strengths and weaknesses across categories",
    "Helps compare profiles or performance between multiple items"
  ],
  "use_cases": [
    "Business: Employee skill assessments, performance reviews",
    "Sports: Player stats comparison (speed, stamina, defense, attack)",
    "Marketing: Customer satisfaction across multiple factors",
    "Education: Student performance across subjects",
    "Product Analysis: Comparing features of competing products"
  ],
  "data_requirements": {
    "categories": "Variables or dimensions to compare (e.g., skills, stats, factors)",
    "values": "Numerical values for each category",
    "series": "One or multiple items/entities to compare across categories"
  }
},
  {
  "chart_id": 23,
  "name": "word_cloud",
  "title": "Word Cloud",
  "why": [
    "To quickly identify the most common words in a dataset",
    "Provides a visual summary of text data",
    "Helps spot themes, patterns, or key topics without deep reading"
  ],
  "use_cases": [
    "Text Analysis: Most frequent words in customer reviews, survey responses, or comments",
    "Marketing: Popular keywords from social media, hashtags, or campaigns",
    "Education/Research: Main topics in articles, books, or research papers",
    "Business: Highlighting product features customers talk about most",
    "Events: Live display of audience feedback or trending discussion words"
  ],
  "data_requirements": {
    "text_data": "Collection of text (e.g., reviews, comments, articles)",
    "frequency": "Word counts or frequencies to determine size",
    "color": "Optional colors to represent categories, themes, or sentiment"
  }
},
  {
  "chart_id": 24,
  "name": "pivot_table",
  "title": "Pivot Table",
  "why": [
    "To quickly analyze large datasets and extract meaningful insights",
    "Makes it easy to slice and dice data from different perspectives",
    "Reduces manual work of writing formulas or queries for every summary"
  ],
  "use_cases": [
    "Business & Sales: Total sales by region, product, or salesperson",
    "Finance: Expense breakdown by category and time period",
    "Marketing: Customer segmentation (age, location, channel)",
    "HR & Operations: Employee count by department, gender, or job role",
    "Education/Research: Survey responses grouped by demographics or answers"
  ],
  "data_requirements": {
    "rows": "Categories or fields to group by (e.g., region, department)",
    "columns": "Optional secondary categories for cross-tabulation",
    "values": "Numerical values to aggregate (e.g., sums, counts, averages)",
    "aggregation": "Method of summarization (sum, count, average, min, max, etc.)"
  }
}
]