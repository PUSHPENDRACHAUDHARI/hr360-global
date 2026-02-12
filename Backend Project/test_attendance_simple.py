#!/usr/bin/env python3
"""
Simple test to verify the attendance records functionality fix
"""
import requests
import time
import re

def test_attendance_records():
    """Test the complete attendance records flow"""
    
    print("Testing Attendance Records Fix")
    print("=" * 50)
    
    # Create a session
    session = requests.Session()
    
    # Step 1: Get login page and CSRF token
    print("1. Getting login page...")
    login_url = "http://127.0.0.1:8000/"
    response = session.get(login_url)
    
    if response.status_code != 200:
        print(f"Failed to get login page: {response.status_code}")
        return False
    
    # Extract CSRF token
    csrf_token = None
    if 'csrfmiddlewaretoken' in response.text:
        match = re.search(r'name="csrfmiddlewaretoken" value="([^"]*)"', response.text)
        if match:
            csrf_token = match.group(1)
            print(f"CSRF token obtained: {csrf_token[:20]}...")
        else:
            print("Failed to extract CSRF token")
            return False
    else:
        print("CSRF token not found in response")
        return False
    
    # Step 2: Login as employee
    print("\n2. Logging in as employee...")
    login_data = {
        'role': 'employee',
        'email': 'testemployee@example.com',
        'password': 'test123',
        'csrfmiddlewaretoken': csrf_token
    }
    
    response = session.post(login_url, data=login_data, allow_redirects=True)
    
    if response.status_code != 200:
        print(f"Login failed: {response.status_code}")
        return False
    
    # Check if we're redirected to dashboard
    if '/employee-dashboard/' in response.url:
        print("Login successful - redirected to employee dashboard")
    else:
        print(f"Login failed - redirected to: {response.url}")
        if 'Invalid' in response.text:
            print("Invalid credentials error")
        return False
    
    # Step 3: Test attendance records access
    print("\n3. Testing attendance records access...")
    attendance_url = "http://127.0.0.1:8000/employee-attendance-records/"
    
    response = session.get(attendance_url)
    
    print(f"   Status Code: {response.status_code}")
    print(f"   Final URL: {response.url}")
    
    if response.status_code == 200:
        if 'My Attendance Records' in response.text:
            print("SUCCESS: Attendance records page loaded successfully!")
            print("   Found page title: 'My Attendance Records'")
            return True
        else:
            print("FAIL: Page loaded but content doesn't match expected")
            # Show first 500 characters for debugging
            print("   Page content preview:")
            print(response.text[:500])
            return False
    elif response.status_code == 302:
        if '/employee-dashboard/' in response.url:
            print("FAIL: Still redirecting to dashboard - authentication issue")
            # Check for error messages
            if 'Please login' in response.text or 'session' in response.text.lower():
                print("   Error: Authentication/session problem detected")
            return False
        else:
            print(f"FAIL: Unexpected redirect to: {response.url}")
            return False
    else:
        print(f"FAIL: Unexpected status code: {response.status_code}")
        print("   Response content:")
        print(response.text[:500])
        return False

def test_button_functionality():
    """Test the dashboard button functionality"""
    print("\n4. Testing dashboard button functionality...")
    
    session = requests.Session()
    
    # Login first
    login_url = "http://127.0.0.1:8000/"
    response = session.get(login_url)
    csrf_token = None
    if 'csrfmiddlewaretoken' in response.text:
        match = re.search(r'name="csrfmiddlewaretoken" value="([^"]*)"', response.text)
        if match:
            csrf_token = match.group(1)
    
    if csrf_token:
        login_data = {
            'role': 'employee',
            'email': 'testemployee@example.com',
            'password': 'test123',
            'csrfmiddlewaretoken': csrf_token
        }
        session.post(login_url, data=login_data, allow_redirects=True)
    
    # Get dashboard page
    dashboard_url = "http://127.0.0.1:8000/employee-dashboard/"
    response = session.get(dashboard_url)
    
    if response.status_code == 200:
        print("Dashboard loaded successfully")
        
        # Look for the attendance records button
        if 'employee-attendance-records' in response.text:
            print("Attendance Records button found in dashboard")
            
            # Try to simulate clicking the button
            attendance_url = "http://127.0.0.1:8000/employee-attendance-records/"
            response = session.get(attendance_url)
            
            if response.status_code == 200 and 'My Attendance Records' in response.text:
                print("SUCCESS: Button click simulation successful - attendance records loaded!")
                return True
            else:
                print(f"FAIL: Button click failed - Status: {response.status_code}")
                return False
        else:
            print("FAIL: Attendance Records button not found in dashboard")
            return False
    else:
        print(f"FAIL: Dashboard failed to load: {response.status_code}")
        return False

if __name__ == "__main__":
    print("Starting Attendance Records Fix Test")
    print("Testing the attendance records button functionality...")
    
    # Test basic functionality
    test1_result = test_attendance_records()
    
    # Test button functionality
    test2_result = test_button_functionality()
    
    print("\n" + "=" * 50)
    print("TEST RESULTS SUMMARY")
    print("=" * 50)
    print(f"1. Basic Attendance Records Test: {'PASS' if test1_result else 'FAIL'}")
    print(f"2. Dashboard Button Test: {'PASS' if test2_result else 'FAIL'}")
    
    if test1_result and test2_result:
        print("\nALL TESTS PASSED! Attendance Records fix is working!")
        exit(0)
    else:
        print("\nTESTS FAILED! Issues still exist with attendance records.")
        exit(1)