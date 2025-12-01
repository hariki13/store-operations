# Data Analysis & Analytics Learning Tasks

## Overview
This document contains progressive tasks designed to enhance your data analysis and data analytics skills using the coffee shop sales dataset. Complete each task in order, as they build upon each other.

---

## 🟢 Level 1: Beginner - Data Fundamentals

### Task 1.1: Data Loading and Exploration
**Objective:** Master basic data loading and initial exploration techniques.

**Instructions:**
1. Create a new Python file called `task_1_1_data_exploration.py`
2. Load the coffee sales dataset
3. Complete the following:
   - Display the first 10 and last 10 rows
   - Show the shape of the dataset (rows, columns)
   - List all column names
   - Display data types for each column
   - Generate summary statistics using `.describe()`

**Expected Output:** A script that prints comprehensive dataset overview.

---

### Task 1.2: Missing Data Analysis
**Objective:** Learn to identify and handle missing data.

**Instructions:**
1. Create `task_1_2_missing_data.py`
2. Implement functions to:
   - Count missing values per column
   - Calculate percentage of missing values
   - Visualize missing data with a heatmap
   - Implement different strategies: drop rows, fill with mean/median/mode

**Skills Practiced:** Data cleaning, visualization, decision-making

---

### Task 1.3: Data Type Conversions
**Objective:** Understand and practice data type conversions.

**Instructions:**
1. Create `task_1_3_data_types.py`
2. Practice conversions:
   - String to datetime
   - String to numeric
   - Numeric to categorical
3. Extract datetime components (year, month, day, hour, weekday)

**Challenge:** Create a function that automatically detects and suggests data type corrections.

---

## 🟡 Level 2: Intermediate - Descriptive Analytics

### Task 2.1: Statistical Measures
**Objective:** Calculate and interpret statistical measures.

**Instructions:**
1. Create `task_2_1_statistics.py`
2. Calculate for the 'money' column:
   - Mean, median, mode
   - Standard deviation and variance
   - Range (min, max)
   - Quartiles (Q1, Q2, Q3)
   - Interquartile Range (IQR)
   - Skewness and Kurtosis
3. Create a function that generates a complete statistical report

**Deliverable:** A reusable function `generate_statistical_report(dataframe, column)`

---

### Task 2.2: Group Analysis
**Objective:** Master groupby operations and aggregations.

**Instructions:**
1. Create `task_2_2_group_analysis.py`
2. Analyze data grouped by:
   - Coffee name: total sales, average price, count
   - Payment method: total transactions, average amount
   - Day of week: busiest days, average sales per day
   - Hour of day: peak hours analysis
3. Use multiple aggregation functions: sum, mean, count, min, max

**Challenge:** Create a pivot table showing sales by coffee type and day of week.

---

### Task 2.3: Advanced Visualization
**Objective:** Create informative and professional visualizations.

**Instructions:**
1. Create `task_2_3_visualizations.py`
2. Create the following visualizations:
   - Histogram of sales distribution
   - Box plot of sales by coffee type
   - Pie chart of sales proportion by product
   - Scatter plot of time vs sales amount
   - Heatmap of correlation matrix
3. Add proper titles, labels, legends, and annotations

**Bonus:** Create a multi-panel figure combining 4 visualizations.

---

## 🟠 Level 3: Advanced - Analytical Techniques

### Task 3.1: Time Series Analysis
**Objective:** Perform comprehensive time series analysis.

**Instructions:**
1. Create `task_3_1_time_series.py`
2. Implement:
   - Daily, weekly, and monthly sales aggregation
   - Moving averages (7-day, 30-day)
   - Year-over-year comparison (if applicable)
   - Seasonal decomposition
   - Trend identification

**Visualization:** Create a time series plot with trend line and moving averages.

---

### Task 3.2: Customer Behavior Analysis
**Objective:** Analyze purchasing patterns and customer behavior.

**Instructions:**
1. Create `task_3_2_customer_analysis.py`
2. Analyze:
   - Popular products at different times of day
   - Payment method preferences
   - Purchase frequency patterns
   - Average transaction value by time period
3. Create customer segments based on purchasing behavior

**Deliverable:** A report identifying key customer insights.

---

### Task 3.3: Anomaly Detection
**Objective:** Identify unusual patterns and outliers in data.

**Instructions:**
1. Create `task_3_3_anomaly_detection.py`
2. Implement detection methods:
   - Z-score method
   - IQR method
   - Visual inspection with box plots
3. Investigate detected anomalies
4. Decide on handling strategy (remove, flag, investigate)

**Challenge:** Create an automated anomaly detection function.

---

## 🔴 Level 4: Expert - Predictive Analytics

### Task 4.1: Sales Forecasting (Simple)
**Objective:** Build basic predictive models for sales forecasting.

**Instructions:**
1. Create `task_4_1_forecasting.py`
2. Implement:
   - Simple moving average prediction
   - Exponential smoothing
   - Linear regression for trend
3. Split data into training and test sets
4. Calculate prediction accuracy (MAE, RMSE)

**Deliverable:** A model that predicts next day's sales.

---

### Task 4.2: Product Recommendation Analysis
**Objective:** Analyze product relationships for recommendations.

**Instructions:**
1. Create `task_4_2_product_analysis.py`
2. Analyze:
   - Products frequently bought together
   - Product affinity analysis
   - Sales correlation between products
3. Create a simple recommendation logic

**Bonus:** Implement market basket analysis if transaction data allows.

---

### Task 4.3: Business Dashboard
**Objective:** Create a comprehensive analytical dashboard.

**Instructions:**
1. Create `task_4_3_dashboard.py`
2. Build a dashboard showing:
   - Key Performance Indicators (KPIs)
   - Sales trends over time
   - Top performing products
   - Hourly/daily patterns
   - Comparison metrics
3. Save as interactive HTML or image report

**Tools:** Consider using Plotly for interactive visualizations.

---

## 📊 Final Project: Complete Store Operations Analysis

### Objective
Combine all learned skills into a comprehensive analysis project.

### Requirements
1. Create `final_project_analysis.py`
2. Include:
   - Complete data cleaning pipeline
   - Comprehensive descriptive statistics
   - Multiple visualization types
   - Time series analysis
   - Customer behavior insights
   - Simple forecasting model
   - Executive summary with key findings

### Deliverables
- Clean, well-commented Python code
- Visualization exports (PNG/HTML)
- Written report (Markdown or PDF) with:
  - Data overview
  - Methodology
  - Key findings
  - Recommendations for the coffee shop
  - Future analysis suggestions

---

## 📚 Additional Resources

### Python Libraries to Learn
- **pandas** - Data manipulation
- **numpy** - Numerical operations
- **matplotlib** - Basic plotting
- **seaborn** - Statistical visualization
- **plotly** - Interactive charts
- **scikit-learn** - Machine learning
- **statsmodels** - Statistical modeling

### Recommended Learning Path
1. Complete tasks in order (1.1 → 1.2 → 1.3 → 2.1 → ...)
2. Don't skip tasks - they build on each other
3. Experiment with variations of each task
4. Document your learnings and challenges

### Tips for Success
- Read the pandas and matplotlib documentation
- Use `.head()` frequently to check your work
- Comment your code explaining your thought process
- Create reusable functions when possible
- Version control your progress with git commits

---

## Progress Tracking

| Task | Status | Date Completed | Notes |
|------|--------|----------------|-------|
| 1.1 | ⬜ | | |
| 1.2 | ⬜ | | |
| 1.3 | ⬜ | | |
| 2.1 | ⬜ | | |
| 2.2 | ⬜ | | |
| 2.3 | ⬜ | | |
| 3.1 | ⬜ | | |
| 3.2 | ⬜ | | |
| 3.3 | ⬜ | | |
| 4.1 | ⬜ | | |
| 4.2 | ⬜ | | |
| 4.3 | ⬜ | | |
| Final Project | ⬜ | | |

Mark tasks as ✅ when completed!

---

*Good luck with your data analytics journey! 🚀*
