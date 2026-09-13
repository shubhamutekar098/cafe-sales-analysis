import pandas as pd

input_file = "data/dirty_cafe_sales.csv"
output_file = "data/cleaned_cafe_sales.csv"

df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)

print("\nMissing values before cleaning:")
print(df.isnull().sum())

df = df.replace(["ERROR", "UNKNOWN"], pd.NA)

duplicates = df.duplicated().sum()
print("\nDuplicate rows:", duplicates)

df = df.drop_duplicates()

text_columns = ["Item", "Payment Method", "Location"]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

numeric_columns = ["Quantity", "Price Per Unit", "Total Spent"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)

for column in text_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())

if df["Transaction Date"].isnull().sum() > 0:
    df["Transaction Date"] = df["Transaction Date"].fillna(
        df["Transaction Date"].mode()[0]
    )

df.loc[df["Quantity"] <= 0, "Quantity"] = df["Quantity"].median()
df.loc[df["Price Per Unit"] <= 0, "Price Per Unit"] = df["Price Per Unit"].median()
df.loc[df["Total Spent"] <= 0, "Total Spent"] = df["Total Spent"].median()

df["Quantity"] = df["Quantity"].round().astype(int)
df["Price Per Unit"] = df["Price Per Unit"].round(2)
df["Total Spent"] = df["Total Spent"].round(2)

df["Calculated Total"] = (
    df["Quantity"] * df["Price Per Unit"]
).round(2)

df.to_csv(output_file, index=False)

print("\nCleaning completed successfully!")
print("Final dataset shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nCleaned file saved at:")
print(output_file)

print("\nFirst 5 rows:")
print(df.head())