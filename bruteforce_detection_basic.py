print("=== Brute Force Detection Basic ===")

failed_logins = 7

if failed_logins > 5:
    print("🚨 Possible Brute Force Attack Detected")
else:
    print("System looks normal")