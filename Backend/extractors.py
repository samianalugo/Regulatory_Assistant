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
    # Look for patterns like "Drug X", "drug ABC", "medication XYZ", etc.
    patterns = [
        r'\b(drug\s+[A-Za-z0-9\-\_]+)\b',  # "Drug X"
        r'\b(medication\s+[A-Za-z0-9\-\_]+)\b',  # "Medication ABC"
        r'\b(medicine\s+[A-Za-z0-9\-\_]+)\b',  # "Medicine XYZ"
        r'\b([A-Z][a-z]+\s+[A-Z][a-z]+)\b',  # "Generic Name" (two capitalized words)
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.I)
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
    """
    Process a medical report and extract structured data
    """
    try:
        print(f"Processing report: {report_text[:100]}...")  # Debug log
        
        result = {
            "drug": extract_drug(report_text),
            "adverse_events": extract_adverse_events(report_text),
            "severity": extract_severity(report_text),
            "outcome": extract_outcome(report_text),
        }
        
        print(f"Extracted result: {result}")  # Debug log
        return result
        
    except Exception as e:
        print(f"Error in process_report_text: {e}")  # Debug log
        # Return default values if processing fails
        return {
            "drug": "Unknown",
            "adverse_events": [],
            "severity": "unknown",
            "outcome": "unknown"
        } 