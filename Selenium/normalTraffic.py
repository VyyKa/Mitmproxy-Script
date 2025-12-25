from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Cấu hình Proxy để đẩy traffic qua Mitmproxy (cổng 8080)
PROXY = "127.0.0.1:8080"
options = webdriver.ChromeOptions()
options.add_argument(f'--proxy-server={PROXY}')
# Chấp nhận chứng chỉ SSL không an toàn từ proxy
options.add_argument('--ignore-certificate-errors') 

driver = webdriver.Chrome(options=options)

def normal_user_flow():
    try:
        # 1. Truy cập trang chủ
        driver.get("http://localhost:3000") # [cite: 30]
        time.sleep(2)
        
        # Tắt các thông báo popup ban đầu của Juice Shop
        try:
            driver.find_element(By.ID, "mat-dialog-0").find_element(By.CLASS_NAME, "close-dialog").click()
            driver.find_element(By.LINK_TEXT, "Dismiss").click()
        except:
            pass

        # 2. Tìm kiếm sản phẩm (Tạo request GET)
        search_box = driver.find_element(By.ID, "searchQuery")
        search_box.send_keys("Apple")
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        # 3. Đăng nhập (Tạo request POST) [cite: 19]
        driver.get("http://localhost:3000/#/login")
        driver.find_element(By.ID, "email").send_keys("demo@juice-sh.op")
        driver.find_element(By.ID, "password").send_keys("demo12345")
        driver.find_element(By.ID, "loginButton").click()
        time.sleep(2)

        # 4. Xem chi tiết sản phẩm và thêm vào giỏ hàng [cite: 19]
        driver.find_element(By.CLASS_NAME, "mat-card").click() # Click sản phẩm đầu tiên
        time.sleep(1)
        # Thêm vào giỏ hàng
        driver.find_element(By.XPATH, "//button[@aria-label='Add to Basket']").click()
        
    finally:
        driver.quit()

if __name__ == "__main__":
    # Lặp lại nhiều lần để tạo dataset lớn
    for i in range(10):
        print(f"Running iteration {i+1}")
        normal_user_flow()