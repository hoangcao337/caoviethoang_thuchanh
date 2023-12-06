import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

# Đọc dữ liệu từ file CSV
data = pd.read_csv('diemsv.csv')

# Xử lý dữ liệu
hours_studied = data['Hours Studied']
performance_index = data['Performance Index']

# Vẽ biểu đồ
plt.figure(figsize=(10,6))
plt.scatter(hours_studied, performance_index, color='blue')
plt.title('Hours Studied vs Performance Index')
plt.xlabel('Hours Studied')
plt.ylabel('Performance Index')
plt.show()
