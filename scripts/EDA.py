import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

input_file = "data/cleaned_cafe_sales.csv"
output_folder = "reports/charts"

os.makedirs(output_folder, exist_ok=True)

df = pd.read_csv(input_file)

df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

df["Month"] = df["Transaction Date"].dt.to_period("M").astype(str)
df["Day"] = df["Transaction Date"].dt.day_name()

total_sales = df["Total Spent"].sum()
total_transactions = len(df)
average_transaction = df["Total Spent"].mean()
total_quantity = df["Quantity"].sum()

print("EDA COMPLETED")
print("\nTotal Sales:", round(total_sales, 2))
print("Total Transactions:", total_transactions)
print("Average Transaction:", round(average_transaction, 2))
print("Total Quantity Sold:", total_quantity)

print("\nSales by Item:")
print(
    df.groupby("Item")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Payment Method:")
print(
    df.groupby("Payment Method")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Location:")
print(
    df.groupby("Location")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

monthly_sales = (
    df.groupby("Month")["Total Spent"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=monthly_sales,
    x="Month",
    y="Total Spent",
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    f"{output_folder}/monthly_sales.png",
    dpi=300
)
plt.show()

item_sales = (
    df.groupby("Item")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
item_sales.plot(kind="bar")
plt.title("Sales by Item")
plt.xlabel("Item")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    f"{output_folder}/sales_by_item.png",
    dpi=300
)
plt.show()

payment_sales = (
    df.groupby("Payment Method")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))
payment_sales.plot(kind="bar")
plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(
    f"{output_folder}/sales_by_payment.png",
    dpi=300
)
plt.show()

location_sales = (
    df.groupby("Location")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))
location_sales.plot(kind="bar")
plt.title("Sales by Location")
plt.xlabel("Location")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(
    f"{output_folder}/sales_by_location.png",
    dpi=300
)
plt.show()

quantity_by_item = (
    df.groupby("Item")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
quantity_by_item.plot(kind="bar")
plt.title("Quantity Sold by Item")
plt.xlabel("Item")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    f"{output_folder}/quantity_by_item.png",
    dpi=300
)
plt.show()

day_sales = (
    df.groupby("Day")["Total Spent"]
    .sum()
    .reindex([
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ])
)

plt.figure(figsize=(10, 6))
day_sales.plot(kind="bar")
plt.title("Sales by Day of Week")
plt.xlabel("Day")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(
    f"{output_folder}/sales_by_day.png",
    dpi=300
)
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(
    df["Total Spent"],
    bins=30,
    kde=True
)
plt.title("Distribution of Transaction Amount")
plt.xlabel("Total Spent")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(
    f"{output_folder}/transaction_distribution.png",
    dpi=300
)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="Quantity",
    y="Total Spent"
)
plt.title("Quantity vs Total Spent")
plt.xlabel("Quantity")
plt.ylabel("Total Spent")
plt.tight_layout()
plt.savefig(
    f"{output_folder}/quantity_vs_sales.png",
    dpi=300
)
plt.show()

print("\nKey Insights")

print(
    "\nTop selling item:",
    item_sales.index[0]
)

print(
    "Highest sales payment method:",
    payment_sales.index[0]
)

print(
    "Highest sales location:",
    location_sales.index[0]
)

print(
    "Best sales day:",
    day_sales.idxmax()
)

print(
    "\nCharts saved in:",
    output_folder
)