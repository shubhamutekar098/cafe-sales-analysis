import pandas as pd

df = pd.read_csv("data/dirty_cafe_sales.csv")

print("Original Data:")
print(df.shape)

# Replace ERROR and UNKNOWN
df = df.replace(["ERROR", "UNKNOWN"], pd.NA)

# Remove duplicate rows
df = df.drop_duplicates()

# Convert numbers
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

# Convert date
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"], errors="coerce"
)

# Fill missing text values
df["Item"] = df["Item"].fillna(df["Item"].mode()[0])
df["Payment Method"] = df["Payment Method"].fillna(df["Payment Method"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# Fill missing numbers
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Price Per Unit"].median())
df["Total Spent"] = df["Total Spent"].fillna(df["Total Spent"].median())

# Fill missing dates
df["Transaction Date"] = df["Transaction Date"].fillna(
    df["Transaction Date"].mode()[0]
)

# Fix zero or negative values
df.loc[df["Quantity"] <= 0, "Quantity"] = df["Quantity"].median()
df.loc[df["Price Per Unit"] <= 0, "Price Per Unit"] = df["Price Per Unit"].median()
df.loc[df["Total Spent"] <= 0, "Total Spent"] = df["Total Spent"].median()

# Save cleaned data
df.to_csv("data/cleaned_cafe_sales.csv", index=False)

print("Cleaning completed!")
print("Final Data:")
print(df.shape)
print(df.head())