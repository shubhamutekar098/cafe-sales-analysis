from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

DATA_FILE = "data/cleaned_cafe_sales.csv"


def load_data():
    df = pd.read_csv(DATA_FILE)
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    return df


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/api/data")
def get_data():
    df = load_data()

    total_sales = df["Total Spent"].sum()
    total_transactions = len(df)
    total_quantity = df["Quantity"].sum()
    average_transaction = df["Total Spent"].mean()

    monthly = (
        df.groupby(df["Transaction Date"].dt.to_period("M"))["Total Spent"]
        .sum()
        .reset_index()
    )

    monthly["Transaction Date"] = monthly["Transaction Date"].astype(str)

    item_sales = (
        df.groupby("Item")["Total Spent"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    payment_sales = (
        df.groupby("Payment Method")["Total Spent"]
        .sum()
        .reset_index()
    )

    location_sales = (
        df.groupby("Location")["Total Spent"]
        .sum()
        .reset_index()
    )

    return jsonify({
        "summary": {
            "total_sales": round(total_sales, 2),
            "total_transactions": total_transactions,
            "total_quantity": int(total_quantity),
            "average_transaction": round(average_transaction, 2)
        },

        "monthly": {
            "labels": monthly["Transaction Date"].tolist(),
            "values": monthly["Total Spent"].round(2).tolist()
        },

        "items": {
            "labels": item_sales["Item"].tolist(),
            "values": item_sales["Total Spent"].round(2).tolist()
        },

        "payments": {
            "labels": payment_sales["Payment Method"].tolist(),
            "values": payment_sales["Total Spent"].round(2).tolist()
        },

        "locations": {
            "labels": location_sales["Location"].tolist(),
            "values": location_sales["Total Spent"].round(2).tolist()
        }
    })
"interpretation": [
    "Juice has the highest sales among all items.",
    "Digital Wallet is the most used payment method.",
    "Takeaway has higher sales than In-store.",
    "Monday has the highest sales among all days.",
    "The monthly chart shows how sales change over time.",
    "The quantity vs sales chart shows the relationship between quantity sold and total spending."
]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
