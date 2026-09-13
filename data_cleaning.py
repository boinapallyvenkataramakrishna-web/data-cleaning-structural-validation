import os
from pathlib import Path
import pandas as pd

# Determine file paths relative to script location
BASE_DIR = Path(__file__).resolve().parent
input_file = BASE_DIR / "sample_dataset.csv"
if not input_file.exists():
    input_file = BASE_DIR / "sample_dataset.csv.csv"

# Load dataset
df = pd.read_csv(input_file)

print("Original Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Records:", df.duplicated().sum())

# Standardize column headers
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

# Remove duplicate rows
df = df.drop_duplicates()

# Clean text columns
for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].str.strip().str.lower()

# Convert date columns
for col in df.columns:
    if "date" in col or "time" in col:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# Fill numeric missing values with median
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical missing values with mode
for col in df.select_dtypes(include=["object", "string"]).columns:
    mode = df[col].mode()
    if not mode.empty:
        df[col] = df[col].fillna(mode.iloc[0])

# Validate
print("\nData Types:\n", df.dtypes)
print("\nMissing Values After Cleaning:\n", df.isnull().sum())
print("\nDuplicates After Cleaning:", df.duplicated().sum())

# Export
output_file = BASE_DIR / "cleaned_dataset.csv"
df.to_csv(output_file, index=False)
print(f"\nSaved: {output_file.name}")
