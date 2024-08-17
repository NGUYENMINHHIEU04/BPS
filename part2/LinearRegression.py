import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Đọc dữ liệu đã xử lý
df = pd.read_csv('sales_data.csv')

# Chuẩn bị dữ liệu
df['SaleDate'] = pd.to_datetime(df['SaleDate'])
df['DateNumeric'] = (df['SaleDate'] - df['SaleDate'].min()).dt.days  # Chuyển đổi ngày thành số

# Tạo biến độc lập (X) và biến phụ thuộc (y)
X = df[['DateNumeric']]
y = df['TotalPrice']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán doanh thu
y_pred = model.predict(X)

# Trực quan hóa kết quả
plt.figure(figsize=(12, 6))
plt.scatter(df['SaleDate'], y, color='blue', label='Doanh Thu Thực Tế')
plt.plot(df['SaleDate'], y_pred, color='red', label='Dự Đoán Doanh Thu', linewidth=2)
plt.title('Dự Đoán Doanh Thu Tương Lai bằng Hồi Quy Tuyến Tính')
plt.xlabel('Ngày')
plt.ylabel('Tổng Doanh Thu')
plt.xticks(rotation=45)
plt.legend()
plt.show()


