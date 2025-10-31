import os
from datetime import datetime, timedelta
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# GraphQL endpoint
transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=True,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

# Calculate date 7 days ago
seven_days_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

# GraphQL query to get orders from the last 7 days
query = gql("""
query GetRecentOrders($startDate: Date!) {
  orders(filter: {order_date_gte: $startDate}) {
    id
    customer {
      email
    }
    order_date
  }
}
""")

params = {"startDate": seven_days_ago}

try:
    result = client.execute(query, variable_values=params)
    orders = result.get("orders", [])

    log_file = "/tmp/order_reminders_log.txt"
    with open(log_file, "a") as f:
        for order in orders:
            order_id = order["id"]
            customer_email = order["customer"]["email"]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - Order ID: {order_id}, Customer Email: {customer_email}\n")

    print("Order reminders processed!")

except Exception as e:
    print(f"Error fetching orders: {e}")

#!/usr/bin/env python3

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime, timedelta

# GraphQL endpoint
transport = RequestsHTTPTransport(url="http://localhost:8000/graphql", verify=False)
client = Client(transport=transport, fetch_schema_from_transport=True)

# Calculate date 7 days ago
seven_days_ago = (datetime.now() - timedelta(days=7)).date()

# GraphQL query to get orders within last 7 days
query = gql("""
query GetRecentOrders($since: Date!) {
  orders(orderDate_Gte: $since) {
    id
    customer {
      email
    }
  }
}
""")

# Execute query
params = {"since": str(seven_days_ago)}
result = client.execute(query, variable_values=params)

# Log file
LOG_FILE = "/tmp/order_reminders_log.txt"

# Log each order
with open(LOG_FILE, "a") as f:
    for order in result.get("orders", []):
        order_id = order["id"]
        email = order["customer"]["email"]
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - Order ID {order_id} for {email}\n")

print("Order reminders processed!")

