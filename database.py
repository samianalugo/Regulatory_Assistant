# database.py
import os
import sqlite3
from datetime import datetime

# Use environment variable DB_PATH; default to a writable per-user dir
DEFAULT_DB_DIR = os.path.join(os.path.expanduser("~"), ".reg_assistant")
DEFAULT_DB_PATH = os.path.join(DEFAULT_DB_DIR, "reports.db")
DB_PATH = os.getenv("DB_PATH", DEFAULT_DB_PATH)
db_conn = None


def init_db():
    """
    Initialize the SQLite database connection and create tables if they don't exist.
    """
    global db_conn
    try:
        # Ensure directory exists
        db_dir = os.path.dirname(DB_PATH)
        if db_dir and not os.path.isdir(db_dir):
            os.makedirs(db_dir, exist_ok=True)

        db_conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        cur = db_conn.cursor()
        
        # Create reports table if it doesn't exist
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
        print(f"Database initialized at {DB_PATH}")
        return db_conn

    except Exception as e:
        print("Failed to initialize database:", e)
        db_conn = None
        raise e


# Optional helper functions for CRUD

def save_report(report_text, extracted):
    """
    Save a processed report to the database.
    'extracted' should be a dictionary with keys: drug, adverse_events, severity, outcome
    """
    global db_conn
    if db_conn is None:
        raise Exception("Database connection not initialized")

    cur = db_conn.cursor()
    now = datetime.utcnow().isoformat()
    cur.execute("""
        INSERT INTO reports (report_text, drug, adverse_events, severity, outcome, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        report_text,
        extracted.get("drug"),
        extracted.get("adverse_events"),
        extracted.get("severity"),
        extracted.get("outcome"),
        now
    ))
    db_conn.commit()
    return cur.lastrowid


def get_reports():
    """
    Fetch all reports from the database.
    """
    global db_conn
    if db_conn is None:
        raise Exception("Database connection not initialized")

    cur = db_conn.cursor()
    cur.execute("SELECT * FROM reports ORDER BY id DESC")
    rows = cur.fetchall()
    # Convert to list of dicts
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "report_text": row[1],
            "drug": row[2],
            "adverse_events": row[3],
            "severity": row[4],
            "outcome": row[5],
            "created_at": row[6]
        })
    return result


def check_integrity():
    """
    Check whether the DB file exists and run PRAGMA integrity_check.
    Returns a dict with keys: exists, db_path, integrity (list) or error, and tables (list).
    """
    try:
        exists = os.path.exists(DB_PATH)
        if not exists:
            return {"exists": False, "db_path": DB_PATH}

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute('PRAGMA integrity_check;')
        integrity = cur.fetchall()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [r[0] for r in cur.fetchall()]
        conn.close()
        return {
            "exists": True,
            "db_path": DB_PATH,
            "integrity": integrity,
            "tables": tables,
        }
    except Exception as e:
        return {"exists": True, "db_path": DB_PATH, "error": str(e)}