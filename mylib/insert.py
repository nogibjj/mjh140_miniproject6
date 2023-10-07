import sqlite3

def insert(dbname: str, tab: str, new_data: dict):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"PRAGMA table_info({tab})")
    columns_info = c.fetchall()
    num_columns = len(columns_info)
    payload = format_data(new_data, columns_info)
    placeholders = ", ".join(["?"] * num_columns)
    c.execute(f"INSERT INTO {tab} VALUES ({placeholders})", payload)
    conn.commit()

def format_data(data: dict, columns_info: list):
    # Cycle through the db columns, determine if there's any new data. 
    # Save new data/NULL values in new_data
    payload = ()
    for item in columns_info:
        _, col_name, _, _, _, _ = item
        payload += (data.get(str(col_name)),)
    print(payload)
    
    return payload