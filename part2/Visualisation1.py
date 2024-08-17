import pandas as pd
import matplotlib.pyplot as plt
# Đọc tệp CSV đã được xử lý
data = pd.read_csv('MarketTrend_Cleaned.csv')
# 1. Biểu đồ cột cho chỉ số phổ biến theo nhóm sản phẩm
plt.figure(figsize=(10, 6))
data.groupby('ProductGroupID')['PopularityIndex'].mean().plot(kind='bar', color='skyblue')
plt.title('Chỉ số phổ biến trung bình theo nhóm sản phẩm')
plt.xlabel('Nhóm sản phẩm')
plt.ylabel('Chỉ số phổ biến trung bình')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
