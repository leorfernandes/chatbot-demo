#!/usr/bin/env python3
"""
Test script to demonstrate the Dialogflow webhook functionality
without needing the frontend integration.

This simulates what Dialogflow would send to your webhook.
"""

import requests
import json

def test_webhook():
    """Test the webhook with a complete conversation flow"""
    base_url = "http://localhost:5000"
    session_id = "test-session-123"
    
    print("TESTING DIALOGFLOW WEBHOOK INTEGRATION")
    print("=" * 50)
    
    # Test if server is running
    try:
        response = requests.get(f"{base_url}/test")
        print(f"Server Status: {response.json()}")
        print()
    except Exception as e:
        print(f"Server not running: {e}")
        print("Please start the backend with: python app.py")
        return
    
    # Complete conversation flow
    conversation_steps = [
        {
            "step": "1. Welcome",
            "data": {
                "queryResult": {
                    "queryText": "hello",
                    "intent": {"displayName": "welcome"},
                    "parameters": {}
                },
                "session": f"projects/demo-project/agent/sessions/{session_id}"
            }
        },
        {
            "step": "2. Collect Name",
            "data": {
                "queryResult": {
                    "queryText": "My name is John",
                    "intent": {"displayName": "collect.basic.info"},
                    "parameters": {"person": {"name": "John"}}
                },
                "session": f"projects/demo-project/agent/sessions/{session_id}"
            }
        },
        {
            "step": "3. Collect Age",
            "data": {
                "queryResult": {
                    "queryText": "I'm 30 years old",
                    "intent": {"displayName": "collect.basic.info"},
                    "parameters": {"age": 30}
                },
                "session": f"projects/demo-project/agent/sessions/{session_id}"
            }
        },
        {
            "step": "4. Collect Location",
            "data": {
                "queryResult": {
                    "queryText": "I live in Seattle",
                    "intent": {"displayName": "collect.basic.info"},
                    "parameters": {"location": "Seattle"}
                },
                "session": f"projects/demo-project/agent/sessions/{session_id}"
            }
        },
        {
            "step": "5. Collect Values",
            "data": {
                "queryResult": {
                    "queryText": "5",
                    "intent": {"displayName": "collect.values"},
                    "parameters": {"number": 5}
                },
                "session": f"projects/demo-project/agent/sessions/{session_id}"
            }
        }
    ]
    
    print("COMPLETE CONVERSATION FLOW")
    print("=" * 40)
    
    for step_info in conversation_steps:
        print(f"\n{step_info['step']}")
        print("-" * 30)
        
        try:
            response = requests.post(
                f"{base_url}/webhook",
                json=step_info['data'],
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"Bot: {result['fulfillmentText']}")
            else:
                print(f"Error {response.status_code}: {response.text}")
                
        except Exception as e:
            print(f"Request failed: {e}")

if __name__ == "__main__":
    test_webhook()
