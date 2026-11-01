import pandas as pd

# Load scraped dataset
df = pd.read_csv("output/quotes.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

# Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Dataset size
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns.tolist())

# Data types
print("\nData types:")
print(df.dtypes)

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing quote or author
df = df.dropna(subset=["Quote", "Author"])

# Remove empty quotes
df = df[df["Quote"].str.strip() != ""]

# Remove extra spaces
df["Quote"] = df["Quote"].str.strip()
df["Author"] = df["Author"].str.strip()
df["Tags"] = df["Tags"].fillna("").str.strip()

# Save cleaned dataset
df.to_csv("output/quotes_cleaned.csv", index=False)

print("\n" + "=" * 50)
print("DATA CLEANING COMPLETED")
print("=" * 50)

print("Final dataset shape:", df.shape)
print("Cleaned file saved as: output/quotes_cleaned.csv")
