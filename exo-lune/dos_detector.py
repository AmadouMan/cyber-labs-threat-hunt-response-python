import requests
from collections import Counter

LOG_URL = "http://192.168.112.144:8088/logs.json"
BLOCK_URL = "http://192.168.112.144:9099"

THRESHOLD = 3
DRY_RUN = False

logs = requests.get(LOG_URL).json()

ips = [l["ip"] for l in logs]
counts = Counter(ips)

suspects = [ip for ip, c in counts.items() if c >= THRESHOLD]

print("\n=== INCIDENT SUMMARY ===")

for ip in suspects:
    print(ip, counts[ip])

    if DRY_RUN:
        print("Would block", ip)
    else:
        requests.post(BLOCK_URL, json={"ip": ip})
