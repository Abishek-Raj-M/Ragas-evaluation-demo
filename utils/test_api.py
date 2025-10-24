#!/usr/bin/env python3
"""
Simple API Test Script
Tests EPAM DIAL API connection without Unicode characters
"""

import os
import requests
from dotenv import load_dotenv

def test_api():
    """Test EPAM DIAL API connection"""
    print("EPAM DIAL API Connection Test")
    print("=" * 40)
    
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv('DIAL_API_KEY')
    azure_endpoint = os.getenv('AZURE_ENDPOINT', 'https://ai-proxy.lab.epam.com')
    api_version = os.getenv('API_VERSION', '2024-02-01')
    
    print(f"API Key: {'Set' if api_key and api_key != 'your_api_key_here' else 'NOT SET'}")
    print(f"Endpoint: {azure_endpoint}")
    print(f"Version: {api_version}")
    
    if not api_key or api_key == 'your_api_key_here':
        print("\nERROR: API Key not set!")
        print("Please create a .env file with your EPAM DIAL API key")
        return False
    
    # Test API connection
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    try:
        url = f"{azure_endpoint}/openai/deployments?api-version={api_version}"
        print(f"\nTesting URL: {url}")
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("SUCCESS: API connection working!")
            data = response.json()
            deployments = data.get('data', [])
            print(f"Found {len(deployments)} deployments")
            return True
        else:
            print(f"ERROR: API returned status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    test_api()
