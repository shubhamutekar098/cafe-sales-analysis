async function loadDashboard() {
    try {
        console.log("Loading dashboard...");

        const response = await fetch("/api/data");

        console.log("API status:", response.status);

        if (!response.ok) {
            throw new Error(`API request failed: ${response.status}`);
        }

        const data = await response.json();

        console.log("API data:", data);

        document.getElementById("totalSales").textContent =
            "₹" + Number(data.summary.total_sales).toLocaleString();

        document.getElementById("totalTransactions").textContent =
            Number(data.summary.total_transactions).toLocaleString();

        document.getElementById("totalQuantity").textContent =
            Number(data.summary.total_quantity).toLocaleString();

        document.getElementById("averageTransaction").textContent =
            "₹" + Number(data.summary.average_transaction).toLocaleString();


        new Chart(document.getElementById("monthlyChart"), {
            type: "line",
            data: {
                labels: data.monthly.labels,
                datasets: [{
                    label: "Total Sales",
                    data: data.monthly.values,
                    fill: false,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });


        new Chart(document.getElementById("itemChart"), {
            type: "bar",
            data: {
                labels: data.items.labels,
                datasets: [{
                    label: "Sales",
                    data: data.items.values
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });


        new Chart(document.getElementById("paymentChart"), {
            type: "doughnut",
            data: {
                labels: data.payments.labels,
                datasets: [{
                    data: data.payments.values
                }]
            },
            options: {
                responsive: true
            }
        });


        new Chart(document.getElementById("locationChart"), {
            type: "bar",
            data: {
                labels: data.locations.labels,
                datasets: [{
                    label: "Sales",
                    data: data.locations.values
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });

        console.log("Dashboard loaded successfully!");

    } catch (error) {
        console.error("Dashboard loading error:", error);
    }
}

loadDashboard();
