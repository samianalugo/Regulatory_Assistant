#!/usr/bin/env python3
"""
Test database connection and operations
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import init_db, db_conn
from crud import save_report, get_reports

def test_database():
    print("🧪 Testing database...")
    
    try:
        # Test database initialization
        print("1. Testing database initialization...")
        conn = init_db()
        print(f"✅ Database initialized: {conn}")
        
        # Test saving a report
        print("2. Testing save_report...")
        test_data = {
            "drug": "Drug X",
            "adverse_events": ["nausea", "headache"],
            "severity": "severe",
            "outcome": "recovered"
        }
        
        report_id = save_report("Test report", test_data)
        print(f"✅ Report saved with ID: {report_id}")
        
        # Test getting reports
        print("3. Testing get_reports...")
        reports = get_reports()
        print(f"✅ Found {len(reports)} reports")
        
        if reports:
            print(f"Latest report: {reports[0]}")
        
        return True
        
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_database()
