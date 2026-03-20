import requests
from collections import Counter


AWS_LOG_URL = "https://example-aws-logs/api/events"
GCP_LOG_URL = "https://example-gcp-logs/api/events"

BLOCK_URL = "http://192.168.112.144:9099"

THRESHOLD = 5
DRY_RUN = True


def fetch_logs(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json()
    except Exception as e:
        print(f"Telemetry fetch failed from {url}: {e}")
        return []



aws_logs = fetch_logs(AWS_LOG_URL)
gcp_logs = fetch_logs(GCP_LOG_URL)


all_ips = []

for event in aws_logs:
    all_ips.append(event.get("source_ip"))

for event in gcp_logs:
    all_ips.append(event.get("source_ip"))


counts = Counter(all_ips)

suspects = [ip for ip, c in counts.items() if c >= THRESHOLD]

print("\n=== MULTI-CLOUD INCIDENT SUMMARY ===")

for ip in suspects:
    print(ip, counts[ip])

    if DRY_RUN:
        print("Would block:", ip)
    else:
        requests.post(BLOCK_URL, json={"ip": ip})
