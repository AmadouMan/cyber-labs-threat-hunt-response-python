print("=== SSH Failed Login Detector ===")

logs = [
    "failed password from 162.168.1.10",
    "accepted password from 10.0.0.5",
    "Failed password from 45.33.22.11",
    "Failed password from 45.33.22.11"
]

count = 0

for line in logs:
    if "failed" in line.lower():
        print("alert:", line)
        count += 1

print("Total:", count)