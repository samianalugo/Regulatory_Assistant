#!/usr/bin/env python3
"""
Test script to check API endpoints
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_api_connection():
    """Test if the API is running"""
    try:
        response = requests.get(f"{BASE_URL}/docs")
        print(f"✅ API is running - Status: {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        return False

def test_process_report():
    """Test the process-report endpoint"""
    print("\n🧪 Testing process-report endpoint...")
    
    test_data = {
        "report": "Patient experienced severe nausea and headache after taking Drug X. Patient recovered."
    }
    
    try:
        response = requests.post(f"{BASE_URL}/process-report", json=test_data)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Success! Response: {json.dumps(result, indent=2)}")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return False

def test_get_reports():
    """Test the get reports endpoint"""
    print("\n🧪 Testing get reports endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/reports")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Success! Found {len(result)} reports")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Testing Regulatory Assistant API...")
    print("=" * 50)
    
    # Test API connection
    if not test_api_connection():
        print("\n❌ API is not running. Please start the backend server first.")
        exit(1)
    
    # Test endpoints
    results = []
    results.append(test_process_report())
    results.append(test_get_reports())
    
    print("\n" + "=" * 50)
    print(f"Tests passed: {sum(results)}/{len(results)}")
    
    if all(results):
        print("✅ All tests passed! API is working correctly.")
    else:
        print("❌ Some tests failed. Check the errors above.")
