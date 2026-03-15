import os
import time

print("\n=== SOC Persistence Hunter v1 ===\n")

startup_paths = [
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"),
    os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
]

suspicious_keywords = [
    "update",
    "service",
    "chrome",
    "svchost",
    "system",
    "winlogon"
]

alerts = []

for path in startup_paths:
    print(f"\n[+] Scanning Startup Path: {path}")

    if not os.path.exists(path):
        print("[!] Path not found")
        continue

    for file in os.listdir(path):

        full_path = os.path.join(path, file)

        try:
            modified_time = os.path.getmtime(full_path)
            age_minutes = (time.time() - modified_time) / 60

            print(f"File: {file} | Last Modified: {round(age_minutes,2)} min ago")

            for keyword in suspicious_keywords:
                if keyword.lower() in file.lower():
                    alerts.append((file, full_path))

        except:
            pass


print("\n====== Persistence Hunting Report ======")

if alerts:
    for file, path in alerts:
        print(f"🚨 Suspicious persistence file: {file}")
        print(f"   Path: {path}")
else:
    print("No obvious suspicious persistence detected.")