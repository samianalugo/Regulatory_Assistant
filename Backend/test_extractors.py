#!/usr/bin/env python3
"""
Test the extractors to see if they're working correctly
"""

# Test the extractors directly
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extractors import process_report_text

def test_extractors():
    print("🧪 Testing extractors...")
    
    test_text = "Patient experienced severe nausea and headache after taking Drug X. Patient recovered."
    
    try:
        result = process_report_text(test_text)
        print(f"✅ Extractors working! Result: {result}")
        
        # Check each field
        print(f"Drug: {result['drug']}")
        print(f"Adverse Events: {result['adverse_events']}")
        print(f"Severity: {result['severity']}")
        print(f"Outcome: {result['outcome']}")
        
        return True
    except Exception as e:
        print(f"❌ Extractors failed: {e}")
        return False

if __name__ == "__main__":
    test_extractors()
