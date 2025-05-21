import numpy as np
import pandas as pd

# Load the diabetes dataset
# Adjust the path if your dataset is stored elsewhere
df = pd.read_csv("diabetes.csv")

# List of columns to treat 0s as missing
cols_to_fix = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

# Count how many 0s are in each of these columns
for col in cols_to_fix:
    print(f"{col} has {(df[col] == 0).sum()} zero values")

# Replace 0s with median values (more robust than mean)
for col in cols_to_fix:
    median_val = df[col].median()
    df[col] = df[col].replace(0, median_val)

# Check if all 0s are gone
print((df[cols_to_fix] == 0).sum())
