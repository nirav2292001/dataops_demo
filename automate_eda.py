import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_csv(input_file, output_file):
    # Read data from CSV
    df = pd.read_csv(input_file)

    # 1. Handle missing values (numerical columns - mean, categorical - mode)
    df.fillna(df.mean(), inplace=True)  # for numerical columns
    df.fillna(df.mode().iloc[0], inplace=True)  # for categorical columns

    # 2. Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # 3. Convert data types (datetime and numeric)
    # Example: Assuming 'DateColumn' exists in your data, replace with actual column names
    if 'DateColumn' in df.columns:
        df['DateColumn'] = pd.to_datetime(df['DateColumn'], errors='coerce')
    
    # Convert numeric columns (replace 'NumericColumn' with actual column names)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 4. Standardize column names (lowercase and replace spaces with underscores)
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # 5. Handle categorical data (One-Hot Encoding)
    df = pd.get_dummies(df, drop_first=True)

    # 6. Handle outliers (using IQR method)
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= (Q1 - 1.5 * IQR)) & (df[col] <= (Q3 + 1.5 * IQR))]

    # 7. Normalize numerical data
    scaler = StandardScaler()
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = scaler.fit_transform(df[[col]])

    # 8. Trim whitespaces in string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # 9. Save cleaned data to new CSV
    df.to_csv(output_file, index=False)

    print(f"Data cleaned and saved to {output_file}")

# Example usage
input_file = 'SampleSuperstore.csv'  # Replace with your actual file path
output_file = 'cleaned_data.csv'    # Name of the cleaned data file
preprocess_csv(input_file, output_file)

