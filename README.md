# Mitmproxy-Script
mitmproxy -s logger.py --listen-port 8080

# SQLmap:
# Chạy SQLmap quét một URL cụ thể và đẩy traffic qua proxy 8080
sqlmap -u "http://localhost:3000/rest/products/search?q=apple" --proxy="http://127.0.0.1:8080" --batch --random-agent --level=1

# Nikto:
# Quét mục tiêu và đẩy toàn bộ request qua Mitmproxy
nikto -h http://localhost:3000 -useproxy http://127.0.0.1:8080