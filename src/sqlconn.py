import os
from databricks import sql
from dotenv import load_dotenv

def sqlConnect():
    # Define your SQL Data Warehouse connection details
    # Load environment variables from .env file
    load_dotenv()

    SERVER_HOSTNAME = os.getenv("SERVER_HOSTNAME")
    TOKEN = os.getenv("ACCESS_TOKEN")
    PATH = os.getenv("HTTP_PATH")

    conn = sql.connect(
        server_hostname=SERVER_HOSTNAME,
        http_path=PATH,
        access_token=TOKEN,
    )
    c = conn.cursor()
    c.execute("SELECT * FROM kenpom_stats")
    rows = c.fetchall()
    for row in rows:
        print(row)

    return conn, "Success"

def sqlClose(conn):
    conn.close()

if __name__ == "__main__":
    sqlConnect()