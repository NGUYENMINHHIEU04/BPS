# sklearn 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Đọc dữ liệu đã xử lý
df = pd.read_csv('sales_data.csv')

# Chuẩn bị dữ liệu
df['SaleDate'] = pd.to_datetime(df['SaleDate'])
df['DateNumeric'] = (df['SaleDate'] - df['SaleDate'].min()).dt.days  # Chuyển đổi ngày thành số

# Tạo biến độc lập (X) và biến phụ thuộc (y)
X = df[['DateNumeric']]
y = df['TotalPrice']

# Xây dựng mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X, y)

# Dự đoán doanh thu
y_pred = model.predict(X)

# Tạo dữ liệu cho dự đoán trong tương lai
future_days = np.array([[i] for i in range(X['DateNumeric'].max() + 1, X['DateNumeric'].max() + 31)])  # Dự đoán cho 30 ngày tiếp theo
future_predictions = model.predict(future_days)

# Tạo dữ liệu cho biểu đồ
future_dates = pd.date_range(start=df['SaleDate'].max() + pd.Timedelta(days=1), periods=30)

# Trực quan hóa kết quả
plt.figure(figsize=(12, 6))
plt.scatter(df['SaleDate'], y, color='blue', label='Doanh Thu Thực Tế')
plt.plot(df['SaleDate'], y_pred, color='red', label='Dự Đoán Doanh Thu', linewidth=2)
plt.plot(future_dates, future_predictions, color='orange', linestyle='--', label='Dự Đoán Doanh Thu Tương Lai', linewidth=2)
plt.title('Dự Đoán Doanh Thu Tương Lai bằng Hồi Quy Tuyến Tính')
plt.xlabel('Ngày')
plt.ylabel('Tổng Doanh Thu')
plt.xticks(rotation=45)
plt.legend()
plt.show()
