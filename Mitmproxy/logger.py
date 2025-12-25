from mitmproxy import http
import csv
import os

# Cấu hình nhãn tấn công (thay đổi nhãn này trước mỗi lần chạy tool scan khác nhau)
CURRENT_LABEL = "SQL_INJECTION" # Các giá trị: NORMAL, SQLI, XSS, RCE, v.v.

class RequestLogger:
    def __init__(self):
        self.filename = "my_custom_dataset.csv"
        # Tạo file và header nếu chưa có
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["raw_request", "label"])

    def request(self, flow: http.HTTPFlow):
        # Lấy raw request theo định dạng chuẩn HTTP
        raw_req = flow.request.assemble().decode('utf-8', 'ignore')
        
        with open(self.filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([raw_req, CURRENT_LABEL])

addons = [RequestLogger()]