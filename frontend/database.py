# backend/database.py
import sqlite3

DB_PATH = "reports.db"
db_conn = None

def init_db():
    global db_conn
    db_conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cur = db_conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_text TEXT NOT NULL,
        drug TEXT,
        adverse_events TEXT,
        severity TEXT,
        outcome TEXT,
        created_at TEXT
    );
    """)
    db_conn.commit()
    return db_conn
