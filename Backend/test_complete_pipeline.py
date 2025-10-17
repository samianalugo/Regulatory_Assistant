#!/usr/bin/env python3
"""
Comprehensive test of the entire processing pipeline
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all imports"""
    print("🧪 Testing imports...")
    
    try:
        from database import init_db, db_conn
        print("✅ Database imports OK")
        
        from crud import save_report, get_reports
        print("✅ CRUD imports OK")
        
        from extractors import process_report_text, extract_drug, extract_adverse_events, extract_severity, extract_outcome
        print("✅ Extractor imports OK")
        
        from models import ReportRequest, ReportResponse
        print("✅ Model imports OK")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_extractors():
    """Test extractor functions individually"""
    print("\n🧪 Testing extractor functions...")
    
    try:
        from extractors import extract_drug, extract_adverse_events, extract_severity, extract_outcome
        
        test_text = "Patient experienced severe nausea and headache after taking Drug X. Patient recovered."
        
        # Test individual functions
        drug = extract_drug(test_text)
        print(f"Drug extraction: {drug}")
        
        events = extract_adverse_events(test_text)
        print(f"Adverse events: {events}")
        
        severity = extract_severity(test_text)
        print(f"Severity: {severity}")
        
        outcome = extract_outcome(test_text)
        print(f"Outcome: {outcome}")
        
        return True
    except Exception as e:
        print(f"❌ Extractor error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_process_report_text():
    """Test the main processing function"""
    print("\n🧪 Testing process_report_text...")
    
    try:
        from extractors import process_report_text
        
        test_text = "Patient experienced severe nausea and headache after taking Drug X. Patient recovered."
        
        result = process_report_text(test_text)
        print(f"Process result: {result}")
        
        # Validate result structure
        required_keys = ['drug', 'adverse_events', 'severity', 'outcome']
        for key in required_keys:
            if key not in result:
                print(f"❌ Missing key: {key}")
                return False
        
        print("✅ Process report text working correctly")
        return True
        
    except Exception as e:
        print(f"❌ Process report text error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_database_operations():
    """Test database operations"""
    print("\n🧪 Testing database operations...")
    
    try:
        from database import init_db
        from crud import save_report, get_reports
        
        # Initialize database
        init_db()
        print("✅ Database initialized")
        
        # Test data
        test_data = {
            "drug": "Drug X",
            "adverse_events": ["nausea", "headache"],
            "severity": "severe",
            "outcome": "recovered"
        }
        
        # Test save
        report_id = save_report("Test report", test_data)
        print(f"✅ Report saved with ID: {report_id}")
        
        # Test get
        reports = get_reports()
        print(f"✅ Retrieved {len(reports)} reports")
        
        return True
        
    except Exception as e:
        print(f"❌ Database operation error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_complete_pipeline():
    """Test the complete pipeline"""
    print("\n🧪 Testing complete pipeline...")
    
    try:
        from extractors import process_report_text
        from crud import save_report
        
        test_text = "Patient experienced severe nausea and headache after taking Drug X. Patient recovered."
        
        # Process the text
        extracted = process_report_text(test_text)
        print(f"Extracted data: {extracted}")
        
        # Save to database
        report_id = save_report(test_text, extracted)
        print(f"✅ Complete pipeline successful! Report ID: {report_id}")
        
        return True
        
    except Exception as e:
        print(f"❌ Complete pipeline error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🔍 Comprehensive Backend Pipeline Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_extractors,
        test_process_report_text,
        test_database_operations,
        test_complete_pipeline
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    print(f"Tests passed: {sum(results)}/{len(results)}")
    
    if all(results):
        print("✅ All tests passed! Backend pipeline is working correctly.")
    else:
        print("❌ Some tests failed. Check the errors above.")
