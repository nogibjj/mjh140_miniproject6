"""Query the database"""

import sqlite3


def query(dbname: str, tab: str):
    """Query the database for the top 5 rows of the specified table"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tab}")
    print(f"Top 5 rows of the {tab} table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


