# backend/crud.py
import json
from datetime import datetime
from database import db_conn

def save_report(report_text: str, extracted: dict) -> int:
    cur = db_conn.cursor()
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
    db_conn.commit()
    return cur.lastrowid

def get_reports():
    cur = db_conn.cursor()
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
