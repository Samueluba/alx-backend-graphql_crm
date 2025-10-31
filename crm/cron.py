from datetime import datetime
import os

# Optional GraphQL check
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

LOG_FILE = "/tmp/crm_heartbeat_log.txt"

def log_crm_heartbeat():
    """Logs a heartbeat message to confirm the CRM app is alive."""
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive\n"

    # Append the message to the log file
    with open(LOG_FILE, "a") as f:
        f.write(message)

    # Optional: Check GraphQL endpoint
    try:
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql("""
        query {
            hello
        }
        """)
        result = client.execute(query)
        # Optional: append GraphQL response to log
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} GraphQL hello response: {result.get('hello')}\n")
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} GraphQL check failed: {e}\n")
