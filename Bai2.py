import numpy as np
from AnhXam import ChuyenDoiAnhSangAnhXam, ChuyenDoiAnhXamSangMaTran, ChuyenDoiMaTranSangAnhXam
from XuLyHisto import VeHistogram, VeHistogramSauCanBang, CanBangHisto, ThuHep, ChuyenDoiSangAnhXamCBTH
from PIL import Image
import matplotlib.pyplot as plt

# Hàm Tích chập 3x3
def TichChap3x3(I, Kernel, n, m):
    filtered_I = []  # Mảng lưu kết quả lọc
    for i in range(1, n-1):  # Duyệt qua từng pixel, bắt đầu từ 1, chạy đến n-2 để tránh lấy pixel ở mép ảnh
        row_result = []  # Mảng lưu kết quả theo hàng
        for j in range(1, m-1):
            neighbors = I[i-1:i+2, j-1:j+2]  # Lấy vùng lân cận 3x3, i-1:i+2 là cách viết ngắn gọn của i-1, i, i+1, j-1:j+2 tương tự
            IChap = np.sum(neighbors * Kernel)  # Tính giá trị tích chập
            row_result.append(IChap)  # Thêm kết quả vào mảng theo hàng
        filtered_I.append(row_result)  # Thêm kết quả của hàng vào mảng kết quả
    return filtered_I

# Hàm Tích chập 5x5
def TichChap5x5(I, Kernel, n, m):
    filtered_I = []  # Mảng lưu kết quả lọc
    for i in range(2, n-2):  # Duyệt qua từng pixel
        row_result = []  # Mảng lưu kết quả theo hàng
        for j in range(2, m-2):
            neighbors = I[i-2:i+3, j-2:j+3]  # Lấy vùng lân cận 5x5
            IChap = np.sum(neighbors * Kernel)  # Tính giá trị tích chập
            row_result.append(IChap)  # Thêm kết quả vào mảng theo hàng
        filtered_I.append(row_result)  # Thêm kết quả của hàng vào mảng kết quả
    return filtered_I

# Hàm Tích chập 7x7
def TichChap7x7(I, Kernel, n, m):
    filtered_I = []  # Mảng lưu kết quả lọc
    for i in range(3, n-3, 2):  # Duyệt qua từng pixel với bước nhảy 2
        row_result = []  # Mảng lưu kết quả theo hàng
        for j in range(3, m-3, 2):
            neighbors = I[i-3:i+4, j-3:j+4]  # Lấy vùng lân cận 7x7
            IChap = np.sum(neighbors * Kernel)  # Tính giá trị tích chập
            row_result.append(IChap)  # Thêm kết quả vào mảng theo hàng
        filtered_I.append(row_result)  # Thêm kết quả của hàng vào mảng kết quả
    return filtered_I

# Hàm thêm padding (đệm) cho ảnh
def addZeropadding(arr, pad):
    return np.pad(arr, pad_width=pad, mode='constant', constant_values=0)  # Thêm 0 xung quanh ảnh

# Hàm lọc trung vị
def median_filter(I):
    n, m = I.shape  # Lấy kích thước ảnh
    filtered_I = np.zeros((n - 2, m - 2))  # Mảng lưu kết quả lọc trung vị
    
    # Duyệt qua từng pixel
    for i in range(1, n-1):
        for j in range(1, m-1):
            # Trích xuất lân cận 3x3, mảng set chứa các giá trị lân cận trùng lặp sẽ tự loại bỏ
            neighbors = {
                I[i - 1, j - 1], I[i - 1, j], I[i - 1, j + 1],
                I[i, j - 1], I[i, j], I[i, j + 1],
                I[i + 1, j - 1], I[i + 1, j], I[i + 1, j + 1]
            } 
            # Sắp xếp và lấy trung vị
            array_sort = sorted(neighbors)
            filtered_I[i - 1, j - 1] = array_sort[len(array_sort) // 2]  # Gán giá trị trung vị cho pixel

    filtered_I = filtered_I.astype(int)  # Chuyển đổi mảng thành kiểu int
    return filtered_I


# Kernel Definitions
Kernel3x3 = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

Kernel5x5 = np.array([
    [1/25, 1/25, 1/25, 1/25, 1/25],
    [1/25, 1/25, 1/25, 1/25, 1/25],
    [1/25, 1/25, 1/25, 1/25, 1/25],
    [1/25, 1/25, 1/25, 1/25, 1/25],
    [1/25, 1/25, 1/25, 1/25, 1/25]
])

Kernel7x7 = np.array([
    [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
    [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
    [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
    [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
    [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
    [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
    [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49],
])

# Main
if __name__ == '__main__':

    print("Chọn ảnh từ 1 đến 10:")
    for i in range(1, 11):
        print(f"{i}. anh{i}.jpg")
    
    choice = int(input("Nhập số của ảnh bạn muốn chọn: "))
    if 1 <= choice <= 11:
        image_path = f"anh{choice}.jpg"
        image = ChuyenDoiAnhSangAnhXam(image_path)
        I = ChuyenDoiAnhXamSangMaTran(image)
        # Image.fromarray(ChuyenDoiAnhSangAnhXam(f"anh{choice}.jpg")).show()
    else:
        print("Lựa chọn không hợp lệ. Sử dụng ảnh mặc định.")
 
    n, m = I.shape # Lấy kích thước ảnh I (n hàng, m cột)
    
    # Menu chọn Kernel 
    print("Chọn Kernel:")
    print("1. 3x3")
    print("2. 5x5")
    print("3. 7x7")
    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        # Kernel 3x3, padding = 1
        array_img = addZeropadding(I, pad=1) # Thêm padding cho ảnh
        a, b = array_img.shape # Lấy kích thước ảnh sau khi thêm padding
        kernel = Kernel3x3 # Sử dụng Kernel 3x3
        I1 = TichChap3x3(array_img, kernel, a, b) # Áp dụng tích chập 3x3
        print("Ảnh I1 (Kernel 3x3, padding = 1):")
        ChuyenDoiMaTranSangAnhXam(np.array(I1)).show() # Hiển thị ảnh I1
        # VeHistogram(np.array(I1), "Histogram của I1") # Vẽ histogram của ảnh I1, tại sao np.array(I1) vì I1 là list, cần chuyển về mảng NumPy

    elif choice == 2:
        # Kernel 5x5, padding = 2
        array_img = addZeropadding(I, pad=2)
        a, b = array_img.shape
        kernel = Kernel5x5
        I2 = TichChap5x5(array_img, kernel, a, b)
        print("Ảnh I2 (Kernel 5x5, padding = 2):")
        ChuyenDoiMaTranSangAnhXam(np.array(I2)).show()
        # VeHistogram(np.array(I2), "Histogram của I2")
        
    elif choice == 3:
        # Kernel 7x7, padding = 3 và stride = 2
        array_img = addZeropadding(I, pad=3)
        a, b = array_img.shape
        kernel = Kernel7x7
        I3 = TichChap7x7(array_img, kernel, a, b)  # Áp dụng stride=2
        print("Ảnh I3 (Kernel 7x7, padding = 3, stride = 2):")
        ChuyenDoiMaTranSangAnhXam(np.array(I3)).show()
        # VeHistogram(np.array(I3), "Histogram của I3")

        # Lọc trung vị ảnh I3 với lân cận 3x3
        I4 = median_filter(np.array(I3))  # Áp dụng lọc trung vị
        print("Ảnh I4 (Sau khi lọc trung vị ảnh I3 với lân cận 3x3):")
        ChuyenDoiMaTranSangAnhXam(np.array(I4)).show()
        # VeHistogram(np.array(I4), "Histogram của I4 (Lọc trung vị)")
        # print(anhTrungVi)
        
        # fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        # axs[1].set_title('Histogram của I4 (Lọc trung vị)')
        # axs[1].hist(np.array(I4).ravel(), bins=256, color='green', alpha=0.7)
        # axs[0].set_title('Histogram của I3')
        # axs[0].hist(np.array(I3).ravel(), bins=256, color='blue', alpha=0.7)
        # plt.show()

    else:
        print("Vui Lòng Chọn Đúng Số!")
        exit()

