"""
Task 1.1: Data Loading and Exploration
======================================
Objective: Master basic data loading and initial exploration techniques.

Instructions:
- Load the coffee sales dataset
- Display the first 10 and last 10 rows
- Show the shape of the dataset (rows, columns)
- List all column names
- Display data types for each column
- Generate summary statistics using .describe()
"""

# --- Step 1: Import Libraries ---
import pandas as pd

# --- Step 2: Load Your Data ---
# TODO: Load the CSV file into a pandas DataFrame
# Hint: Use pd.read_csv('coffee sales dataset.csv')
df = None  # Replace None with your code


# --- Step 3: Display First and Last Rows ---
def display_data_preview(dataframe, n_rows=10):
    """
    Display the first and last n rows of the dataframe.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to preview
    n_rows : int
        Number of rows to display (default 10)
    """
    # TODO: Implement this function
    # Hint: Use .head() and .tail()
    pass


# --- Step 4: Get Dataset Shape ---
def get_dataset_shape(dataframe):
    """
    Print the shape of the dataset (rows, columns).
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to analyze
    """
    # TODO: Implement this function
    # Hint: Use .shape attribute
    pass


# --- Step 5: List Column Names ---
def list_columns(dataframe):
    """
    List all column names in the dataframe.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to analyze
    """
    # TODO: Implement this function
    # Hint: Use .columns attribute
    pass


# --- Step 6: Display Data Types ---
def display_data_types(dataframe):
    """
    Display data types for each column.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to analyze
    """
    # TODO: Implement this function
    # Hint: Use .dtypes attribute or .info() method
    pass


# --- Step 7: Generate Summary Statistics ---
def generate_statistics(dataframe):
    """
    Generate summary statistics for numeric columns.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        The dataframe to analyze
    """
    # TODO: Implement this function
    # Hint: Use .describe() method
    pass


# --- Main Execution ---
if __name__ == "__main__":
    print("=" * 50)
    print("Task 1.1: Data Loading and Exploration")
    print("=" * 50)
    
    # TODO: Call your functions here to complete the task
    # Example:
    # df = pd.read_csv('coffee sales dataset.csv')
    # display_data_preview(df)
    # get_dataset_shape(df)
    # etc.
    
    print("\n--- Task 1.1 Complete! ---")
