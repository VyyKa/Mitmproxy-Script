import pandas as pd

def clean_dataset(input_file, output_file):
    # 1. Đọc dữ liệu từ file CSV đã thu thập
    df = pd.read_csv(input_file)
    print(f"Tổng số request ban đầu: {len(df)}")

    # 2. Loại bỏ các request trùng lặp hoàn toàn (Duplicate)
    # Bước này quan trọng vì các tool scan thường gửi lại cùng 1 payload nhiều lần
    df.drop_duplicates(subset=['raw_request'], keep='first', inplace=True)
    
    # 3. Phân loại Label tổng quát (Anomalous/Normal) dựa trên Attack Type
    # Nếu Attack Type khác 'NORMAL' thì Label là 'Anomalous'
    df['label'] = df['label'].apply(lambda x: 'Normal' if x == 'NORMAL' else 'Anomalous')

    # 4. Lưu kết quả ra file mới
    df.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"Tổng số request sau khi làm sạch: {len(df)}")
    print(f"Phân bổ nhãn:\n{df['label'].value_counts()}")
    print(f"Dataset hoàn thiện đã được lưu tại: {output_file}")

if __name__ == "__main__":
    clean_dataset("my_custom_dataset.csv", "final_llm_dataset.csv")