"""
Task 2.1: Statistical Measures
==============================
Objective: Calculate and interpret statistical measures.

Instructions:
- Calculate mean, median, mode for the 'money' column
- Calculate standard deviation and variance
- Calculate range (min, max)
- Calculate quartiles (Q1, Q2, Q3) and IQR
- Calculate skewness and kurtosis
- Create a reusable statistical report function
"""

# --- Step 1: Import Libraries ---
import pandas as pd
import numpy as np
from scipy import stats

# --- Step 2: Load Your Data ---
# TODO: Load and clean the data (refer to project 1 for cleaning steps)
df = None  # Replace with your code


# --- Step 3: Basic Statistics Functions ---
def calculate_central_tendency(series):
    """
    Calculate measures of central tendency.
    
    Parameters:
    -----------
    series : pd.Series
        The numeric series to analyze
        
    Returns:
    --------
    dict : Dictionary containing mean, median, and mode
    """
    # TODO: Calculate and return mean, median, mode
    # Hint: Use .mean(), .median(), .mode()
    return {
        'mean': None,
        'median': None,
        'mode': None
    }


def calculate_dispersion(series):
    """
    Calculate measures of dispersion.
    
    Parameters:
    -----------
    series : pd.Series
        The numeric series to analyze
        
    Returns:
    --------
    dict : Dictionary containing std, variance, range
    """
    # TODO: Calculate standard deviation, variance, min, max, range
    # Hint: Use .std(), .var(), .min(), .max()
    return {
        'std': None,
        'variance': None,
        'min': None,
        'max': None,
        'range': None
    }


def calculate_quartiles(series):
    """
    Calculate quartiles and IQR.
    
    Parameters:
    -----------
    series : pd.Series
        The numeric series to analyze
        
    Returns:
    --------
    dict : Dictionary containing Q1, Q2, Q3, and IQR
    """
    # TODO: Calculate quartiles
    # Hint: Use .quantile([0.25, 0.5, 0.75])
    return {
        'Q1': None,
        'Q2': None,
        'Q3': None,
        'IQR': None
    }


def calculate_shape_measures(series):
    """
    Calculate skewness and kurtosis.
    
    Parameters:
    -----------
    series : pd.Series
        The numeric series to analyze
        
    Returns:
    --------
    dict : Dictionary containing skewness and kurtosis
    """
    # TODO: Calculate skewness and kurtosis
    # Hint: Use .skew() and .kurtosis() or scipy.stats
    return {
        'skewness': None,
        'kurtosis': None
    }


# --- Step 4: Complete Statistical Report ---
def generate_statistical_report(dataframe, column):
    """
    Generate a comprehensive statistical report for a column.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe containing the data
    column : str
        The column name to analyze
        
    Returns:
    --------
    dict : Complete statistical report
    """
    series = dataframe[column]
    
    # TODO: Combine all statistical measures into one report
    # Call all the functions above and combine results
    
    report = {
        'column_name': column,
        'count': None,
        'central_tendency': calculate_central_tendency(series),
        'dispersion': calculate_dispersion(series),
        'quartiles': calculate_quartiles(series),
        'shape': calculate_shape_measures(series)
    }
    
    return report


def print_statistical_report(report):
    """
    Print the statistical report in a formatted way.
    
    Parameters:
    -----------
    report : dict
        The statistical report dictionary
    """
    print(f"\n{'='*50}")
    print(f"Statistical Report for: {report['column_name']}")
    print(f"{'='*50}")
    
    # TODO: Print all statistics in a readable format
    # Example:
    # print(f"Count: {report['count']}")
    # print(f"\nCentral Tendency:")
    # print(f"  Mean: {report['central_tendency']['mean']:.2f}")
    # etc.
    
    pass


# --- Main Execution ---
if __name__ == "__main__":
    print("=" * 50)
    print("Task 2.1: Statistical Measures")
    print("=" * 50)
    
    # TODO: Complete the task by:
    # 1. Loading and cleaning the data
    # 2. Generating statistical report for 'money' column
    # 3. Printing the report
    # 4. Interpreting the results
    
    # Example interpretation questions:
    # - Is the data normally distributed? (check skewness)
    # - Are there outliers? (compare mean vs median, check IQR)
    # - What is the typical sale amount? (median)
    
    print("\n--- Task 2.1 Complete! ---")
