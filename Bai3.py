import numpy as np
from AnhXam import ChuyenDoiAnhSangAnhXam, ChuyenDoiAnhXamSangMaTran, ChuyenDoiMaTranSangAnhXam
from XuLyHisto import VeHistogram, VeHistogramSauCanBang, CanBangHisto, ChuyenDoiSangAnhXamCBTH
import matplotlib.pyplot as plt

# Hàm so sánh pixel
def SoSanhPixel(value_temp, array_temp):
    array_bit = np.array([])  # Tạo mảng rỗng để lưu kết quả
    # Duyệt qua từng giá trị trong mảng array_temp
    for value in array_temp:
        # So sánh giá trị tạm thời với các giá trị trong mảng
        if(value_temp <= value):
            # Nếu giá trị tạm thời nhỏ hơn hoặc bằng, thêm 1 vào mảng kết quả
            array_bit = np.append(array_bit, 1)
        else:
            # Nếu giá trị tạm thời lớn hơn, thêm 0 vào mảng kết quả
            array_bit = np.append(array_bit, 0)
    return array_bit  # Trả về mảng kết quả

# Hàm đảo ngược bit và cho ra giá trị thập phân
def TinhGiaTriThapPhan(array_bit):
    # Ép kiểu mảng về số nguyên (int)
    array_bit = array_bit.astype(int)
    # Tính giá trị thập phân từ mảng bit
    value = 0
    # Duyệt qua tất cả các phần tử trong mảng bit và tính giá trị thập phân
    for i in range(0, len(array_bit)):
        value += array_bit[i] * pow(2, i)  # Lũy thừa của 2 để tính giá trị thập phân
    return value

# Hàm xuất Cân bằng Histogram
def XuatCanBangHisto(matrix):
    for key, value in matrix.items():
        print(str(key)+ " " + str(value))

# Menu LBP
def LBP(array_img, r, n, m):
    if(r == 1):
        x = LBP1(array_img, n, m) # Lấy ma trận LBP r = 1
        # print("Ma trận LBP r = 1:")
        # print(x)
        # Show ảnh xám LBP r = 1
        ChuyenDoiMaTranSangAnhXam(np.array(x)).show()

        VeHistogram(x, "Histogram của LBP r = 1")

        print("Cân Bằng Histogram")
        a, b = CanBangHisto(x) # a là kết quả cân bằng, b là kết quả trước khi nhóm k, trước khi làm tròn k nhưng không sử dụng b vì nó không cần thiết trong bài này
        
        # XuatCanBangHisto(b)
        VeHistogramSauCanBang(a, "Histogram cân bằng của LBP r = 1")
        # print(b)
        
        # c = ChuyenDoiSangAnhXamCBTH(x, b) # c là ma trận ảnh sau khi cân bằng histogram
        # ChuyenDoiMaTranSangAnhXam(c).show() # hiện ảnh sau khi cân bằng histogram

    elif(r == 2):
        x, y = LBP2(array_img, n, m) 
        # Show ảnh xám LBP r = 2
        ChuyenDoiMaTranSangAnhXam(np.array(x)).show()
        ChuyenDoiMaTranSangAnhXam(np.array(y)).show()
        # ChuyenDoiMaTranSangAnhXam(np.array(avg)).show()
        # Vẽ histogram cho từng bit của ảnh LBP
        VeHistogram(x, "Histogram của 8-bit cao")
        VeHistogram(y, "Histogram của 8-bit thấp")
        # VeHistogram(avg, "Histogram của 8-bit kết hợp")

        # fig, axs = plt.subplots(1, 3, figsize=(12, 6))
        # axs[2].set_title('Histogram của bit kết hợp')
        # axs[2].hist(avg.ravel(), bins=256, color='red', alpha=0.7) #alpha: độ trong suốt
        # axs[1].set_title('Histogram của 8-bit thấp')
        # axs[1].hist(y.ravel(), bins=256, color='green', alpha=0.7) 
        # axs[0].set_title('Histogram của 8-bit cao')
        # axs[0].hist(x.ravel(), bins=256, color='blue', alpha=0.7)
        # plt.show()

        # Ve histogram cho bit kết hợp
        print("Ma trận kết hợp:")
        a = NoiMaTran(x, y)
        # print(a)
        ChuyenDoiMaTranSangAnhXam(np.array(a)).show()
        VeHistogram(a, "Histogram bit kết hợp")

        print("Cân Bằng Histogram")
        x1, x2 = CanBangHisto(x) # x1 là kết quả cân bằng, x2 là kết quả trước khi nhóm k, trước khi làm tròn k nhưng không sử dụng b vì nó không cần thiết trong bài này
        y1, y2 = CanBangHisto(y)
        # avg1, avg2 = CanBangHisto(avg)
        a1, a2 = CanBangHisto(a)
        # Vẽ histogram sau cân bằng
    
        # # Hiển thị 2 histogram sau khi cân bằng
        VeHistogramSauCanBang(x1, "Histogram cân bằng của 8-bit cao")

        VeHistogramSauCanBang(y1, "Histogram cân bằng của 8-bit thấp")

        VeHistogramSauCanBang(a1, "Histogram cân bằng của bit kết hợp")

        # axs = plt.subplots(1, 3, figsize=(12, 6))[1]
        # axs[2].hist(np.array(list(avg1.keys())).ravel(), bins=256, color='red', alpha=0.7, weights=np.array(list(avg1.values())).ravel())
        # axs[2].set_title('Histogram cân bằng của bit kết hợp')
        # axs[1].hist(np.array(list(y1.keys())).ravel(), bins=256, color='green', alpha=0.7, weights=np.array(list(y1.values())).ravel())
        # axs[1].set_title('Histogram cân bằng của 8-bit thấp')
        # axs[0].hist(np.array(list(x1.keys())).ravel(), bins=256, color='blue', alpha=0.7, weights=np.array(list(x1.values())).ravel())
        # axs[0].set_title('Histogram cân bằng của 8-bit cao')
        # plt.show()

    elif(r == 3):
        x, y, z = LBP3(array_img, n, m) 

        # Show ảnh xám LBP r = 3
        ChuyenDoiMaTranSangAnhXam(np.array(x)).show()
        ChuyenDoiMaTranSangAnhXam(np.array(y)).show()
        ChuyenDoiMaTranSangAnhXam(np.array(z)).show()
        # ChuyenDoiMaTranSangAnhXam(np.array(avg)).show()
        # Vẽ histogram cho từng bit của ảnh LBP

        # fig, axs = plt.subplots(1, 4, figsize=(12, 6))
        # axs[3].set_title('Histogram của 8-bit kết hợp')
        # axs[3].hist(avg.ravel(), bins=256, color='purple', alpha=0.7) #.ravel(): chuyển ma trận thành mảng 1 chiều
        # axs[2].set_title('Histogram của 8-bit trung bình')
        # axs[2].hist(z.ravel(), bins=256, color='red', alpha=0.7)
        # axs[1].set_title('Histogram của 8-bit thấp')
        # axs[1].hist(y.ravel(), bins=256, color='green', alpha=0.7)
        # axs[0].set_title('Histogram của 8-bit cao')
        # axs[0].hist(x.ravel(), bins=256, color='blue', alpha=0.7)
        # plt.show()

        VeHistogram(x, "Histogram của 8-bit cao")
        VeHistogram(y, "Histogram của 8-bit thấp")
        VeHistogram(z, "Histogram của 8-bit trung bình")
        # VeHistogram(avg, "Histogram của kết hợp")

        # Ve histogram cho bit kết hợp
        print("Ma trận kết hợp:")
        a = NoiMaTran(x, y, z)
        # print(a)
        ChuyenDoiMaTranSangAnhXam(np.array(a)).show()
        VeHistogram(a, "Histogram của bit kết hợp")

        #Cân bằng histogram
        x1, x2 = CanBangHisto(x) # x1 là kết quả cân bằng, x2 là kết quả trước khi nhóm k, trước khi làm tròn k nhưng không sử dụng b vì nó không cần thiết trong bài này
        y1, y2 = CanBangHisto(y)
        z1, z2 = CanBangHisto(z)
        a1, a2 = CanBangHisto(a)
        # avg1, avg2 = CanBangHisto(avg)

        #Vẽ histogram sau cân bằng
        print("Cân Bằng Histogram")
        VeHistogramSauCanBang(x1, "Histogram cân bằng của 8-bit cao")
        VeHistogramSauCanBang(y1, "Histogram cân bằng của 8-bit thấp")
        VeHistogramSauCanBang(z1, "Histogram cân bằng của 8-bit trung bình")
        # VeHistogramSauCanBang(avg1, "Histogram cân bằng của bit kết hợp")

        VeHistogramSauCanBang(a1, "Histogram cân bằng của bit kết hợp")

        # axs = plt.subplots(1, 4, figsize=(12, 6))[1] 
        # axs[3].hist(np.array(list(avg1.keys())).ravel(), bins=256, color='purple', alpha=0.7, weights=np.array(list(avg1.values())).ravel())
        # axs[3].set_title('Histogram cân bằng của bit kết hợp')
        # axs[2].hist(np.array(list(z1.keys())).ravel(), bins=256, color='red', alpha=0.7, weights=np.array(list(z1.values())).ravel())
        # axs[2].set_title('Histogram cân bằng của 8-bit trung bình')
        # axs[1].hist(np.array(list(y1.keys())).ravel(), bins=256, color='green', alpha=0.7, weights=np.array(list(y1.values())).ravel())
        # axs[1].set_title('Histogram cân bằng của 8-bit thấp')
        # axs[0].hist(np.array(list(x1.keys())).ravel(), bins=256, color='blue', alpha=0.7, weights=np.array(list(x1.values())).ravel())
        # axs[0].set_title('Histogram cân bằng của 8-bit cao')
        # plt.show()
        
# Hàm giải LBP với R = 1
def LBP1(array_img, n, m):
    array_result = np.zeros((n-2, m-2))  # Khởi tạo mảng kết quả
    # Mặc định bước nhảy là 1
    for i in range(1, n-1, 1):
        for j in range(1, m-1, 1): 
            value_temp = array_img[i, j]  # Giá trị của pixel trung tâm
            # Lấy các pixel lân cận (8 pixel xung quanh pixel trung tâm)
            array_temp = [array_img[i,j+1], array_img[i+1,j+1], array_img[i+1, j],
                          array_img[i+1, j-1], array_img[i, j-1], array_img[i-1, j-1],
                          array_img[i-1, j], array_img[i-1, j+1]]
            
            array_bit = SoSanhPixel(value_temp, array_temp)  # So sánh giá trị pixel
            array_result[i-1, j-1] = TinhGiaTriThapPhan(array_bit)  # Tính giá trị nhị phân
            
    return array_result.astype(int)  # Trả về kết quả dưới dạng int

# Hàm giải LBP với R = 2
def LBP2(array_img, n, m):
    array_result1, array_result2 = np.zeros((n-4, m-4)), np.zeros((n-4, m-4))  # Khởi tạo 2 mảng kết quả
    # array_average = np.zeros((n-4, m-4))  
    # Mặc định bước nhảy là 1
    for i in range(2, n-2, 1):
        for j in range(2, m-2, 1):
            value_temp = array_img[i, j]  # Giá trị của pixel trung tâm
            # Lấy các pixel lân cận (16 pixel xung quanh pixel trung tâm)
            array_temp = [
                array_img[i, j+2], array_img[i+1, j+2], array_img[i+2, j+2], array_img[i+2, j+1],
                array_img[i+2, j], array_img[i+2, j-1], array_img[i+2, j-2], array_img[i+1, j-2],
                array_img[i, j-2], array_img[i-1, j-2], array_img[i-2, j-2], array_img[i-2, j-1],
                array_img[i-2, j], array_img[i-2, j+1], array_img[i-2, j+2], array_img[i-1, j+2]
            ]
            array_bit = SoSanhPixel(value_temp, array_temp)  # So sánh giá trị pixel
            high_8bit = array_bit[:8]  # Lấy 8 bit đầu tiên
            low_8bit = array_bit[8:]  # Lấy 8 bit còn lại
            array_result1[i-2, j-2] = TinhGiaTriThapPhan(high_8bit)  # Tính giá trị nhị phân cho high_8bit
            array_result2[i-2, j-2] = TinhGiaTriThapPhan(low_8bit)  # Tính giá trị nhị phân cho low_8bit

            # array_average[i-2, j-2] = np.mean([array_result1[i-2, j-2], array_result2[i-2, j-2]]) # Tính giá trị trung bình của 2 nhóm bit
    return array_result1.astype(int), array_result2.astype(int) # Trả về kết quả

# Hàm giải LBP với R = 3
def LBP3(array_img, n, m):
    array_result1, array_result2, array_result3 = np.zeros((n-6, m-6)), np.zeros((n-6, m-6)), np.zeros((n-6, m-6))  # Khởi tạo 3 mảng kết quả
    # array_average = np.zeros((n-6, m-6)) 
    # Duyệt qua mỗi pixel trong ma trận
    for i in range(3, n-3):  
        for j in range(3, m-3):  
            value_temp = array_img[i, j]  # Giá trị của pixel trung tâm

            # Lấy các pixel lân cận trong bán kính R=3 (24 pixel xung quanh pixel trung tâm)
            array_temp = [
                    array_img[i, j + 3], array_img[i + 1, j + 3], array_img[i + 2, j + 3], array_img[i + 3, j + 3],
                    array_img[i + 3, j + 2], array_img[i + 3, j + 1], array_img[i + 3, j], array_img[i + 3, j - 1],
                    array_img[i + 3, j - 2], array_img[i + 3, j - 3], array_img[i + 2, j - 3], array_img[i + 1, j - 3],
                    array_img[i, j - 3], array_img[i - 1, j - 3], array_img[i - 2, j - 3], array_img[i - 3, j - 3],
                    array_img[i - 3, j - 2], array_img[i - 3, j - 1], array_img[i - 3, j], array_img[i - 3, j + 1],
                    array_img[i - 3, j + 2], array_img[i - 3, j + 3], array_img[i - 2, j + 3], array_img[i - 1, j + 3]
                    ]
            
            # So sánh giá trị của pixel trung tâm với các pixel lân cận
            array_bit = SoSanhPixel(value_temp, array_temp)
            
            high_8bit = array_bit[:8]  # Lấy 8 bit đầu tiên
            low_8bit = array_bit[16:24]  # Lấy 8 bit cuối cùng
            mid_8bit = array_bit[8:16]  # Lấy 8 bit giữa
            
            # Tính giá trị thập phân cho từng nhóm bit
            array_result1[i-3, j-3] = TinhGiaTriThapPhan(high_8bit)
            array_result2[i-3, j-3] = TinhGiaTriThapPhan(low_8bit)
            array_result3[i-3, j-3] = TinhGiaTriThapPhan(mid_8bit) 

            # array_average[i-3, j-3] = np.mean([array_result1[i-3, j-3], array_result2[i-3, j-3], array_result3[i-3, j-3]]) # Tính giá trị trung bình của 3 nhóm bit 

    return array_result1.astype(int), array_result2.astype(int), array_result3.astype(int) # Trả về kết quả

# Hàm thêm padding bằng 0 vào ma trận
def addZeropadding(arr):
    return np.pad(arr, pad_width=1, mode='constant', constant_values=0)  # Thêm padding bằng 0

# Hàm nối ma trận theo chiều nhất định (axis=0 là theo chiều dọc, axis=1 là theo chiều ngang)
def NoiMaTran(*args, axis=0):
    result = np.concatenate(args, axis=axis)  # Nối các ma trận theo chiều axis
    return result  # Trả về ma trận đã nối

# Main
if __name__ == '__main__':
    # Menu chọn ảnh từ 1 đến 10
    array_img = None
    print("Chọn ảnh từ 1 đến 10:")
    for i in range(1, 11):
        print(f"{i}. anh{i}.jpg")
    
    choice = int(input("Nhập số của ảnh bạn muốn chọn: "))
    if 1 <= choice <= 10:
        image_path = f"anh{choice}.jpg"
        image = ChuyenDoiAnhSangAnhXam(image_path)
        array_img = ChuyenDoiAnhXamSangMaTran(image)
    else:
        print("Lựa chọn không hợp lệ. Sử dụng ảnh mặc định.")

    # Cho phép chọn padding
    padding = int(input("Mời bạn chọn zeropadding(0/1): "))
    n, m = array_img.shape
    if(padding == 1):
        array_img = addZeropadding(array_img)
        n, m = array_img.shape

    # Menu chọn R
    luaChon = int(input("Mời bạn chọn R(1/2/3): "))
    LBP(array_img, luaChon, n, m)

