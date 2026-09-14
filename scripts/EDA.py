import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/cleaned_cafe_sales.csv")

os.makedirs("reports/charts", exist_ok=True)

df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

df["Month"] = df["Transaction Date"].dt.to_period("M").astype(str)
df["Day"] = df["Transaction Date"].dt.day_name()

# Basic information
total_sales = df["Total Spent"].sum()
total_transactions = len(df)
average_transaction = df["Total Spent"].mean()
total_quantity = df["Quantity"].sum()

print("EDA COMPLETED")
print("Total Sales:", round(total_sales, 2))
print("Total Transactions:", total_transactions)
print("Average Transaction:", round(average_transaction, 2))
print("Total Quantity Sold:", total_quantity)

# Sales by item
item_sales = df.groupby("Item")["Total Spent"].sum().sort_values(ascending=False)
print("\nSales by Item:")
print(item_sales)

# Sales by payment method
payment_sales = df.groupby("Payment Method")["Total Spent"].sum().sort_values(ascending=False)
print("\nSales by Payment Method:")
print(payment_sales)

# Sales by location
location_sales = df.groupby("Location")["Total Spent"].sum().sort_values(ascending=False)
print("\nSales by Location:")
print(location_sales)

# Monthly sales
monthly_sales = df.groupby("Month")["Total Spent"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/charts/monthly_sales.png")
plt.show()

# Sales by item chart
plt.figure(figsize=(10, 5))
item_sales.plot(kind="bar")
plt.title("Sales by Item")
plt.xlabel("Item")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/charts/sales_by_item.png")
plt.show()

# Sales by payment method
plt.figure(figsize=(8, 5))
payment_sales.plot(kind="bar")
plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("reports/charts/sales_by_payment.png")
plt.show()

# Sales by location
plt.figure(figsize=(8, 5))
location_sales.plot(kind="bar")
plt.title("Sales by Location")
plt.xlabel("Location")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("reports/charts/sales_by_location.png")
plt.show()

# Quantity sold by item
quantity_by_item = df.groupby("Item")["Quantity"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
quantity_by_item.plot(kind="bar")
plt.title("Quantity Sold by Item")
plt.xlabel("Item")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/charts/quantity_by_item.png")
plt.show()

# Sales by day
day_sales = df.groupby("Day")["Total Spent"].sum()

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_sales = day_sales.reindex(days)

plt.figure(figsize=(10, 5))
day_sales.plot(kind="bar")
plt.title("Sales by Day of Week")
plt.xlabel("Day")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("reports/charts/sales_by_day.png")
plt.show()

# Transaction distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Total Spent"], bins=30)
plt.title("Distribution of Transaction Amount")
plt.xlabel("Total Spent")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("reports/charts/transaction_distribution.png")
plt.show()

# Quantity vs sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Quantity", y="Total Spent")
plt.title("Quantity vs Total Spent")
plt.xlabel("Quantity")
plt.ylabel("Total Spent")
plt.tight_layout()
plt.savefig("reports/charts/quantity_vs_sales.png")
plt.show()

# Key insights
print("\nKey Insights")
print("Top selling item:", item_sales.index[0])
print("Highest sales payment method:", payment_sales.index[0])
print("Highest sales location:", location_sales.index[0])
print("Best sales day:", day_sales.idxmax())

print("\nCharts saved in: reports/charts")