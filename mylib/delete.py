import sqlite3

def delete(dbname: str, tab:str, cond_col:str, cond_val:str):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"DELETE FROM {tab} WHERE {cond_col} = '{cond_val}'")
    conn.commit()