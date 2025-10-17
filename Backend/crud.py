# backend/crud.py
import json
from datetime import datetime
from fastapi import HTTPException
from . import database


def _get_conn():
    """Return a live database connection, initializing DB if needed."""
    if database.db_conn is None:
        database.init_db()
    return database.db_conn

def save_report(report_text: str, extracted: dict) -> int:
    """Save a processed report to the database"""
    try:
        # Ensure database is initialized and get live conn
        conn = _get_conn()
        print(f"Saving report with data: {extracted}")  # Debug log
        
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO reports (report_text, drug, adverse_events, severity, outcome, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            report_text,
            extracted.get("drug"),
            json.dumps(extracted.get("adverse_events", [])),
            extracted.get("severity"),
            extracted.get("outcome"),
            datetime.utcnow().isoformat()
        ))
        conn.commit()
        report_id = cur.lastrowid
        print(f"Report saved successfully with ID: {report_id}")  # Debug log
        return report_id
        
    except Exception as e:
        print(f"Error saving report: {e}")  # Debug log
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to save report: {str(e)}")

def get_reports():
    # Ensure database is initialized and get live conn
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, report_text, drug, adverse_events, severity, outcome, created_at FROM reports ORDER BY id DESC")
    rows = cur.fetchall()
    results = []
    for r in rows:
        results.append({
            "id": r[0],
            "report_text": r[1],
            "drug": r[2],
            "adverse_events": json.loads(r[3]) if r[3] else [],
            "severity": r[4],
            "outcome": r[5],
            "created_at": r[6]
        })
    return results
