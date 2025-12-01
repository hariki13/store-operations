"""
Task 3.1: Time Series Analysis
==============================
Objective: Perform comprehensive time series analysis.

Instructions:
- Implement daily, weekly, and monthly sales aggregation
- Calculate moving averages (7-day, 30-day)
- Perform year-over-year comparison (if applicable)
- Implement seasonal decomposition
- Identify trends
"""

# --- Step 1: Import Libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# For advanced time series (optional - you can uncomment when ready)
# from statsmodels.tsa.seasonal import seasonal_decompose

# --- Step 2: Load and Prepare Data ---
# TODO: Load the CSV file and convert datetime column
df = None  # Replace with your code


# --- Step 3: Time Aggregation Functions ---
def aggregate_by_period(dataframe, date_column, value_column, period='D'):
    """
    Aggregate data by time period.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to aggregate
    date_column : str
        Name of the datetime column
    value_column : str
        Name of the value column to aggregate
    period : str
        Time period - 'D' (day), 'W' (week), 'M' (month), 'Y' (year)
        
    Returns:
    --------
    pd.Series : Aggregated time series
    """
    # TODO: Implement this function
    # Hint: Use .set_index(date_column).resample(period)[value_column].sum()
    pass


def get_daily_sales(dataframe, date_column='datetime', value_column='money'):
    """Get daily aggregated sales."""
    # TODO: Implement
    pass


def get_weekly_sales(dataframe, date_column='datetime', value_column='money'):
    """Get weekly aggregated sales."""
    # TODO: Implement
    pass


def get_monthly_sales(dataframe, date_column='datetime', value_column='money'):
    """Get monthly aggregated sales."""
    # TODO: Implement
    pass


# --- Step 4: Moving Averages ---
def calculate_moving_average(series, window):
    """
    Calculate moving average for a time series.
    
    Parameters:
    -----------
    series : pd.Series
        The time series data
    window : int
        The window size for moving average
        
    Returns:
    --------
    pd.Series : Moving average series
    """
    # TODO: Implement this function
    # Hint: Use .rolling(window=window).mean()
    pass


def add_moving_averages(dataframe, value_column, windows=[7, 30]):
    """
    Add multiple moving averages to the dataframe.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to modify (should be indexed by date)
    value_column : str
        Name of the value column
    windows : list
        List of window sizes
        
    Returns:
    --------
    pd.DataFrame : DataFrame with added moving average columns
    """
    # TODO: Implement this function
    # Add columns like 'MA_7', 'MA_30' etc.
    pass


# --- Step 5: Trend Analysis ---
def identify_trend(series):
    """
    Identify the overall trend in the data.
    
    Parameters:
    -----------
    series : pd.Series
        The time series data
        
    Returns:
    --------
    dict : Trend analysis results
    """
    # TODO: Implement basic trend identification
    # Compare first half average vs second half average
    # Or use linear regression to get slope
    
    return {
        'direction': None,  # 'upward', 'downward', 'stable'
        'slope': None,
        'first_period_avg': None,
        'last_period_avg': None
    }


# --- Step 6: Visualization ---
def plot_time_series_with_trend(series, ma_series_dict=None, title='Sales Over Time'):
    """
    Plot time series data with trend lines.
    
    Parameters:
    -----------
    series : pd.Series
        The main time series
    ma_series_dict : dict, optional
        Dictionary of moving average series {'MA_7': series1, 'MA_30': series2}
    title : str
        Plot title
    """
    # TODO: Implement visualization
    # Create a line plot with original data and moving averages
    # Add proper labels, legend, and title
    pass


def plot_seasonal_pattern(daily_sales, title='Average Sales by Day of Week'):
    """
    Plot seasonal/weekly patterns.
    
    Parameters:
    -----------
    daily_sales : pd.Series
        Daily sales series with datetime index
    title : str
        Plot title
    """
    # TODO: Group by day of week and plot average sales
    # Hint: daily_sales.groupby(daily_sales.index.dayofweek).mean()
    pass


# --- Step 7: Advanced - Seasonal Decomposition (Optional) ---
def decompose_time_series(series, period=7):
    """
    Decompose time series into trend, seasonal, and residual components.
    
    Parameters:
    -----------
    series : pd.Series
        The time series to decompose
    period : int
        The seasonal period (7 for weekly, 30 for monthly)
        
    Returns:
    --------
    Decomposition object with .trend, .seasonal, .resid attributes
    """
    # TODO: Implement using statsmodels
    # from statsmodels.tsa.seasonal import seasonal_decompose
    # result = seasonal_decompose(series, period=period)
    # return result
    pass


# --- Main Execution ---
if __name__ == "__main__":
    print("=" * 50)
    print("Task 3.1: Time Series Analysis")
    print("=" * 50)
    
    # TODO: Complete the task by:
    # 1. Loading and preparing data
    # 2. Creating daily, weekly, monthly aggregations
    # 3. Calculating moving averages
    # 4. Identifying trends
    # 5. Creating visualizations
    # 6. (Optional) Performing seasonal decomposition
    
    # Key questions to answer:
    # - What is the overall sales trend?
    # - Which days of the week have highest sales?
    # - Are there any seasonal patterns?
    # - How do moving averages help smooth the data?
    
    print("\n--- Task 3.1 Complete! ---")
