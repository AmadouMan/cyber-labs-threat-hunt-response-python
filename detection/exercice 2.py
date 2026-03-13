failed_logins = 8
source_ip = "45.33.22.11"
country = "RU"
is_blacklisted  = True

print("Checking security event...\n")

if failed_logins > 5:
    print("f high number of failed logins from {source_ip}")
   
if is_blacklisted:
    print("f Alert: IP {source_ip} is blaclisted!")
    
if country != "PL":
    print("f Suspicious login from foreign country: {country}")