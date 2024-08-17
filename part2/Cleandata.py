import pandas as pd
# Đọc tệp CSV
data = pd.read_csv('MarketTrend.csv')
# Hiển thị thông tin tổng quan về dữ liệu
print("Tổng quan dữ liệu:")
print(data.info())
# Kiểm tra và xử lý dữ liệu trống
print("\nSố lượng dữ liệu trống trong mỗi cột:")
print(data.isnull().sum())
# Xử lý dữ liệu trống: loại bỏ hàng có dữ liệu trống
data_cleaned = data.dropna()
# Hoặc thay thế dữ liệu trống bằng giá trị mặc định, ví dụ: "Không xác định"
# data.fillna("Không xác định", inplace=True)
# Kiểm tra và xử lý dữ liệu lỗi
# Giả sử bạn muốn kiểm tra các giá trị không hợp lệ trong cột 'PopularityIndex'
# (có thể là giá trị không nằm trong khoảng 0-100)
data_cleaned = data_cleaned[(data_cleaned['PopularityIndex'] >= 0) & (data_cleaned['PopularityIndex'] <= 100)]
# Hiển thị dữ liệu đã được xử lý
print("\nDữ liệu sau khi xử lý:")
print(data_cleaned)
# Lưu dữ liệu đã xử lý vào tệp mới
data_cleaned.to_csv('MarketTrend_Cleaned.csv', index=False)
