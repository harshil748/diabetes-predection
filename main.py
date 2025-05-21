import pandas as pd

# Load dataset
df = pd.read_csv('diabetes.csv')

# Show first 5 rows
print(df.head())

# Check for missing/null values
print(df.info())
print(df.isnull().sum())