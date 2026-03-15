import os

print("\n=== SOC IOC Scanner v1 ===\n")

log_file = input("Enter log file path: ")
ioc_file = input("Enter IOC file path: ")

# Load IOCs
iocs = set()

# Indent everything under 'with' and 'for'
with open(ioc_file, "r") as f:
    for line in f:
        # line.strip() removes extra spaces or newlines
        iocs.add(line.strip())

print(f"\nLoaded {len(iocs)} IOCs")
print("\n====== Scan Results ======")

# Indent everything under 'with', then 'for', then 'if'
with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        for ioc in iocs:
            if ioc in line:
                print(f"[IOC MATCH] {ioc} -> {line.strip()}")
