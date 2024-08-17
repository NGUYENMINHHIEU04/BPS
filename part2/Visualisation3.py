# 2. Biểu đồ tròn cho tỷ lệ ảnh hưởng doanh số theo nhóm sản phẩm
import pandas as pd
import matplotlib.pyplot as plt
# Đọc tệp CSV đã được xử lý
data = pd.read_csv('MarketTrend_Cleaned.csv')
plt.figure(figsize=(10, 6))
plt.scatter(data['AgeGroup'].apply(lambda x: int(x.split('-')[0])), data['PopularityIndex'], alpha=0.5, color='red')
plt.title('Chỉ số phổ biến theo độ tuổi')
plt.xlabel('Độ tuổi (tuổi)')
plt.ylabel('Chỉ số phổ biến')
plt.grid()
plt.show()