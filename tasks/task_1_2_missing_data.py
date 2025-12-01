"""
Task 1.2: Missing Data Analysis
===============================
Objective: Learn to identify and handle missing data.

Instructions:
- Count missing values per column
- Calculate percentage of missing values
- Visualize missing data with a heatmap
- Implement different strategies: drop rows, fill with mean/median/mode
"""

# --- Step 1: Import Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 2: Load Your Data ---
# TODO: Load the CSV file
df = None  # Replace with your code


# --- Step 3: Count Missing Values ---
def count_missing_values(dataframe):
    """
    Count and display missing values per column.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to analyze
        
    Returns:
    --------
    pd.Series : Count of missing values per column
    """
    # TODO: Implement this function
    # Hint: Use .isnull().sum()
    pass


# --- Step 4: Calculate Missing Percentage ---
def calculate_missing_percentage(dataframe):
    """
    Calculate the percentage of missing values per column.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to analyze
        
    Returns:
    --------
    pd.Series : Percentage of missing values per column
    """
    # TODO: Implement this function
    # Hint: (missing_count / total_rows) * 100
    pass


# --- Step 5: Visualize Missing Data ---
def visualize_missing_data(dataframe, save_path=None):
    """
    Create a heatmap visualization of missing data.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to visualize
    save_path : str, optional
        Path to save the visualization
    """
    # TODO: Implement this function
    # Hint: Use seaborn heatmap with dataframe.isnull()
    pass


# --- Step 6: Handle Missing Data Strategies ---
def fill_with_mean(dataframe, column):
    """
    Fill missing values in a column with the mean.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to modify
    column : str
        Column name to fill
        
    Returns:
    --------
    pd.DataFrame : DataFrame with filled values
    """
    # TODO: Implement this function
    pass


def fill_with_median(dataframe, column):
    """
    Fill missing values in a column with the median.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to modify
    column : str
        Column name to fill
        
    Returns:
    --------
    pd.DataFrame : DataFrame with filled values
    """
    # TODO: Implement this function
    pass


def fill_with_mode(dataframe, column):
    """
    Fill missing values in a column with the mode.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to modify
    column : str
        Column name to fill
        
    Returns:
    --------
    pd.DataFrame : DataFrame with filled values
    """
    # TODO: Implement this function
    pass


def drop_missing_rows(dataframe, columns=None):
    """
    Drop rows with missing values.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to modify
    columns : list, optional
        Specific columns to check for missing values
        
    Returns:
    --------
    pd.DataFrame : DataFrame with dropped rows
    """
    # TODO: Implement this function
    # Hint: Use .dropna(subset=columns) if columns specified
    pass


# --- Main Execution ---
if __name__ == "__main__":
    print("=" * 50)
    print("Task 1.2: Missing Data Analysis")
    print("=" * 50)
    
    # TODO: Complete the task by:
    # 1. Loading the data
    # 2. Analyzing missing values
    # 3. Visualizing missing data
    # 4. Testing different fill strategies
    
    print("\n--- Task 1.2 Complete! ---")
