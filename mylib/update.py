import sqlite3

def update(dbname, tab, col, n_val, cond_col, cond_val):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"UPDATE {tab} SET {col} = ? WHERE {cond_col} = ?", (n_val, cond_val))
    conn.commit()