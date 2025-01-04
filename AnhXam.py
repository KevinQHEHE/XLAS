import cv2
import numpy as np
from PIL import Image

# Chuyển đổi ảnh màu sang ảnh xám
def ChuyenDoiAnhSangAnhXam(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE) # Sử dụng OpenCV (cv2.imread) để đọc ảnh image với tham số cv2.IMREAD_GRAYSCALE, tự động chuyển ảnh sang dạng grayscale.
    return img # Trả về ảnh xám

# Chuyển đổi ảnh xám sang ma trận
def ChuyenDoiAnhXamSangMaTran(image):
    return np.array(image) # Chuyển ảnh xám thành mảng NumPy

# Chuyển đổi ma trận sang ảnh xám
def ChuyenDoiMaTranSangAnhXam(matrix):
    matrix = np.array(matrix) # Chuyển ma trận thành mảng NumPy
    return Image.fromarray(matrix.astype('uint8'), mode='L') # Chuyển ma trận thành ảnh xám, mode='L' là chế độ ảnh xám