import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

def automate_eda(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    print("Data Loaded Successfully")
    
    # Step 1: Initial Data Inspection
    print("Dataset Info:")
    print(data.info())
    print("\nFirst few rows of the data:")
    print(data.head())
    
    # Step 2: Handling Missing Values
    missing_data = data.isnull().sum()
    print("\nMissing Data:")
    print(missing_data[missing_data > 0])  # Show only columns with missing values
    
    # Optionally, you can fill missing values with default options:
    # For example, fill numeric columns with median and categorical with mode:
    data = data.apply(lambda col: col.fillna(col.median()) if col.dtype in ['float64', 'int64'] else col.fillna(col.mode()[0]))
    
    # Step 3: Descriptive Statistics
    print("\nDescriptive Statistics:")
    print(data.describe())
    
    # Step 4: Correlation Analysis
    corr = data.corr()
    print("\nCorrelation Matrix:")
    print(corr)
    
    # Step 5: Categorical Data Analysis
    cat_cols = data.select_dtypes(include=['object']).columns
    print("\nCategorical Columns Analysis:")
    for col in cat_cols:
        print(f"Unique values in {col}: {data[col].unique()}")
        print(f"Most frequent value in {col}: {data[col].mode()[0]}")
    
    # Step 6: Profiling (Optional: Detailed EDA Report using pandas_profiling)
    profile = ProfileReport(data, title="EDA Report", explorative=True)
    profile.to_file("eda_report.html")

    print("\nEDA Report Generated: 'eda_report.html'")

# Example usage:
if __name__ == "__main__":
    file_path = 'your_dataset.csv'  # Replace with your dataset file path
    automate_eda(file_path)
