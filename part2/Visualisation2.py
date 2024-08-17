# 2. Biểu đồ tròn cho tỷ lệ ảnh hưởng doanh số theo nhóm sản phẩm
import pandas as pd
import matplotlib.pyplot as plt
# Đọc tệp CSV đã được xử lý
data = pd.read_csv('MarketTrend_Cleaned.csv')
sales_impact_counts = data['SalesImpact'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(sales_impact_counts, labels=sales_impact_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'gold'])
plt.title('Tỷ lệ ảnh hưởng doanh số theo nhóm sản phẩm')
plt.axis('equal')  
plt.show()

