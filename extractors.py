import re 
from typing import List, Optional

COMMON_EVENTS = ["nausea", "headache", "vomiting", "rash", "fever", "dizziness"]

SEVERITY_KEYWORDS = {
    "severe": ["severe", "life-threatening"],
    "moderate": ["moderate"],
    "mild": ["mild"]
}

OUTCOME_KEYWORDS = {
    "recovered": ["recovered", "resolved", "improved"],
    "ongoing": ["ongoing", "still", "persistent"],
    "fatal": ["fatal", "died", "death"]
}

def extract_drug(text: str) -> Optional[str]:
    match = re.search(r'\b(drug\s+[A-Za-z0-9\-\_]+)\b', text, flags=re.I)
    if match:
        return match.group(1)

    return "Unknown"

def extract_adverse_events(text: str) -> List[str]:
    return [evt for evt in COMMON_EVENTS if evt.lower() in text.lower()]


def extract_severity(text: str) -> str:
    text_lower = text.lower()
    for level, kws in SEVERITY_KEYWORDS.items():
        if any(kw in text_lower for kw in kws):
            return level
    return "unknown"


def extract_outcome(text: str) -> str:
    text_lower = text.lower()
    for label, kws in OUTCOME_KEYWORDS.items():
        if any(kw in text_lower for kw in kws):
            return label
    return "unknown"

def process_report_text(report_text: str) -> dict:
    return {
        "drug": extract_drug(report_text),
        "adverse_events": extract_adverse_events(report_text),
        "severity": extract_severity(report_text),
        "outcome": extract_outcome(report_text),
    } 