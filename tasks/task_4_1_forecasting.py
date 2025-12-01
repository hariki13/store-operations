"""
Task 4.1: Sales Forecasting (Simple)
====================================
Objective: Build basic predictive models for sales forecasting.

Instructions:
- Implement simple moving average prediction
- Implement exponential smoothing
- Implement linear regression for trend
- Split data into training and test sets
- Calculate prediction accuracy (MAE, RMSE)
"""

# --- Step 1: Import Libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# --- Step 2: Load and Prepare Data ---
# TODO: Load and prepare your daily sales data
df = None  # Replace with your code


# --- Step 3: Data Preparation for Forecasting ---
def prepare_forecasting_data(daily_sales):
    """
    Prepare data for forecasting by creating features.
    
    Parameters:
    -----------
    daily_sales : pd.Series
        Daily sales with datetime index
        
    Returns:
    --------
    pd.DataFrame : DataFrame with features for forecasting
    """
    # TODO: Create features like:
    # - Day of week (0-6)
    # - Month (1-12)
    # - Day of month (1-31)
    # - Previous day sales (lag 1)
    # - Previous week same day (lag 7)
    # - Moving average
    pass


def train_test_split_time_series(data, test_size=0.2):
    """
    Split time series data maintaining temporal order.
    
    Parameters:
    -----------
    data : pd.DataFrame or pd.Series
        The time series data
    test_size : float
        Proportion of data for testing
        
    Returns:
    --------
    tuple : (train_data, test_data)
    """
    # TODO: Split data maintaining chronological order
    # Don't shuffle! Use the last test_size% as test data
    pass


# --- Step 4: Forecasting Methods ---
def simple_moving_average_forecast(series, window=7):
    """
    Forecast using simple moving average.
    
    Parameters:
    -----------
    series : pd.Series
        Historical sales data
    window : int
        Moving average window
        
    Returns:
    --------
    float : Forecasted value for next period
    """
    # TODO: Calculate the average of the last 'window' observations
    pass


def exponential_smoothing_forecast(series, alpha=0.3):
    """
    Forecast using exponential smoothing.
    
    Parameters:
    -----------
    series : pd.Series
        Historical sales data
    alpha : float
        Smoothing parameter (0 < alpha < 1)
        
    Returns:
    --------
    pd.Series : Smoothed series with forecast
    """
    # TODO: Implement exponential smoothing
    # Formula: S_t = alpha * Y_t + (1-alpha) * S_{t-1}
    # The forecast is the last smoothed value
    pass


def linear_regression_forecast(train_data, test_data, feature_cols, target_col):
    """
    Forecast using linear regression.
    
    Parameters:
    -----------
    train_data : pd.DataFrame
        Training data with features
    test_data : pd.DataFrame
        Test data with features
    feature_cols : list
        List of feature column names
    target_col : str
        Target column name
        
    Returns:
    --------
    tuple : (model, predictions)
    """
    # TODO: Implement linear regression forecasting
    # 1. Separate features and target
    # 2. Create and fit model
    # 3. Make predictions
    pass


# --- Step 5: Evaluation Metrics ---
def calculate_mae(actual, predicted):
    """
    Calculate Mean Absolute Error.
    
    Parameters:
    -----------
    actual : array-like
        Actual values
    predicted : array-like
        Predicted values
        
    Returns:
    --------
    float : MAE value
    """
    # TODO: Calculate MAE
    # Hint: mean(|actual - predicted|)
    pass


def calculate_rmse(actual, predicted):
    """
    Calculate Root Mean Squared Error.
    
    Parameters:
    -----------
    actual : array-like
        Actual values
    predicted : array-like
        Predicted values
        
    Returns:
    --------
    float : RMSE value
    """
    # TODO: Calculate RMSE
    # Hint: sqrt(mean((actual - predicted)**2))
    pass


def calculate_mape(actual, predicted):
    """
    Calculate Mean Absolute Percentage Error.
    
    Parameters:
    -----------
    actual : array-like
        Actual values
    predicted : array-like
        Predicted values
        
    Returns:
    --------
    float : MAPE value (as percentage)
    """
    # TODO: Calculate MAPE
    # Hint: mean(|actual - predicted| / actual) * 100
    pass


def evaluate_forecast(actual, predicted, model_name="Model"):
    """
    Evaluate forecast accuracy with multiple metrics.
    
    Parameters:
    -----------
    actual : array-like
        Actual values
    predicted : array-like
        Predicted values
    model_name : str
        Name of the model for display
        
    Returns:
    --------
    dict : Dictionary of metrics
    """
    # TODO: Calculate and return all metrics
    return {
        'model': model_name,
        'MAE': None,
        'RMSE': None,
        'MAPE': None
    }


# --- Step 6: Visualization ---
def plot_forecast_comparison(actual, predictions_dict, title='Forecast Comparison'):
    """
    Plot actual values vs multiple forecasts.
    
    Parameters:
    -----------
    actual : pd.Series
        Actual values
    predictions_dict : dict
        Dictionary of {model_name: predictions}
    title : str
        Plot title
    """
    # TODO: Create a plot comparing actual values with forecasts
    # Use different colors for each model
    pass


def plot_residuals(actual, predicted, title='Residual Analysis'):
    """
    Plot residuals (errors) for forecast evaluation.
    
    Parameters:
    -----------
    actual : array-like
        Actual values
    predicted : array-like
        Predicted values
    title : str
        Plot title
    """
    # TODO: Create residual plots
    # 1. Residuals over time
    # 2. Histogram of residuals
    pass


# --- Main Execution ---
if __name__ == "__main__":
    print("=" * 50)
    print("Task 4.1: Sales Forecasting")
    print("=" * 50)
    
    # TODO: Complete the task by:
    # 1. Loading and preparing daily sales data
    # 2. Creating features for forecasting
    # 3. Splitting data into train/test
    # 4. Implementing each forecasting method
    # 5. Evaluating each method
    # 6. Comparing results
    # 7. Creating visualizations
    
    # Key questions to answer:
    # - Which forecasting method performs best?
    # - What is the expected error in predictions?
    # - What features are most important for predictions?
    # - How could the models be improved?
    
    print("\n--- Task 4.1 Complete! ---")
