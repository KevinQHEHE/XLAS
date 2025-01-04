import matplotlib.pyplot as plt
import numpy as np

# Hàm vẽ histogram của ma trận
def VeHistogram(matrix, title):    
    # Chuyển ma trận thành mảng 1 chiều
    data = matrix.flatten()

    # Vẽ histogram với màu sắc "blue" và số lượng bin (cột) (được đặt thành 257), rwidth=0.9: Độ rộng tương đối của các cột
    plt.hist(data, bins=257, edgecolor='black', color='blue', rwidth=0.9) 
    plt.title(title)  # Tiêu đề cho đồ thị
    
    plt.xlabel('Giá Trị')  # Nhãn cho trục X
    plt.ylabel('Tần Suất')  # Nhãn cho trục Y
    
    # Đặt giới hạn cho trục X và Y để tránh xuất hiện các giá trị trùng lặp
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    
    # Hiển thị đồ thị
    plt.show()

def VeHistogramSauCanBang(hist_dict, title):
    # Chuyển keys và values của dict sang danh sách
    keys = list(hist_dict.keys())
    values = list(hist_dict.values())
    
    # Vẽ biểu đồ dạng cột (bar chart) từ keys và values
    plt.bar(keys, values, color='blue', edgecolor='black', width=0.9)
    
    # Thiết lập tiêu đề và nhãn trục
    plt.title(title)
    plt.xlabel('Giá Trị')  # Trục X đại diện cho keys
    plt.ylabel('Tần Suất')  # Trục Y đại diện cho values
    
    # Đặt giới hạn cho trục X và Y
    plt.xlim(left=0, right=256)   # Thêm khoảng trống nhỏ ở đầu/cuối
    plt.ylim(bottom=0)  # Giá trị Y không âm
    
    # Hiển thị biểu đồ
    plt.show()

# Hàm cân bằng histogram
def CanBangHisto(matrix):
    # Tạo một dictionary để lưu trữ giá trị và số lần xuất hiện 
    dict = {} # dict chứa các giá trị và thông tin liên quan
    data = matrix.flatten() # Chuyển ma trận thành mảng 1 chiều
    data = sorted(data) # Sắp xếp mảng theo thứ tự tăng dần

    # Đếm số lần xuất hiện của từng giá trị trong ma trận
    for i in range(len(data)):
        if(data[i] in dict):
            dict[data[i]]["Nk"] += 1 # Nếu giá trị đã có trong dict, tăng số lần xuất hiện lên 1 
        else: 
            dict[data[i]] = {"Nk": 1} # Nếu chưa có, khởi tạo với số lần xuất hiện là 1, ví dụ như: dict = {1: {"Nk": 1}, 2: {"Nk": 1}, 3: {"Nk": 1}, ...}

    # Tính số lượng giá trị duy nhất (L) và tổng số phần tử (n) của ma trận
    L = len(set(dict.keys())) 
    n = matrix.shape[0]*matrix.shape[1] # Tính tổng số phần tử của ma trận, shape[0] là số hàng, shape[1] là số cột
    Sk = 0
    # print(dict)

    # print("L =", L)
    # print("n =", n)

    # Tính các giá trị Pk, Sk và K cho từng giá trị trong dictionary
    for key in dict: # Duyệt qua từng giá trị trong dict
        dict[key]["Pk"] = dict[key]["Nk"]/n  # Xác suất Pk, công thức Pk = Nk/n
        Sk += dict[key]["Pk"]  # Cộng dồn Sk
        dict[key]["Sk"] = Sk # Gán giá trị Sk vào dict
        K = Sk*(L-1)  # Tính giá trị K
        dict[key]["K"] = K # Gán giá trị K vào dict
        
        # Làm tròn K và gán vào Round(k)
        if K - int(K) >= 0.5: # Ví dụ K= 0.476, làm tròn K - int(K) = 0.476 - 0 = 0.476 <= 0.5 => Round(k) = 0
            dict[key]['Round(k)'] = int(K) + 1 # Làm tròn k
        else:
            dict[key]['Round(k)'] = int(K) 
    
    # In ra dictionary chứa các giá trị và thông tin liên quan
    # print(dict)

    # Tạo dictionary mới để nhóm các giá trị có Round(k) giống nhau
    result_dict = {}

    # Duyệt qua các phần tử trong dictionary cũ và nhóm theo Round(k)
    for key, value in dict.items():
        round_k = value['Round(k)']
        nk = value['Nk']

        # Nếu Round(k) đã có trong kết quả, cộng thêm nk vào
        if round_k in result_dict:
            result_dict[round_k] += nk # Cộng thêm số lần xuất hiện vào, key là giá trị Round(k)
        else:
            # Nếu chưa có, khởi tạo mới với giá trị nk
            result_dict[round_k] = nk # Khởi tạo giá trị mới

    # print(result_dict)
    # Trả về kết quả nhóm theo Round(k)
    return result_dict, dict # dict là kết quả sau khi làm tròn k trước khi nhóm theo Round(k) chỉ có round(k) và nk, result_dict là kết quả sau khi nhóm theo Round(k)

# Hàm thu hẹp giá trị của ma trận theo phạm vi
def ThuHep(dict):
    dict_temp= {} 
    for key, value in dict.items(): # Duyệt qua từng phần tử trong dict ở là kết quả sau khi cân bằng histogram
        dict_temp[key] = {"rk":key, "nk":value} # Tạo một dictionary mới với các giá trị ban đầu
    
    # Đặt giá trị Smin và Smax để thu hẹp giá trị
    Smin = 50 
    Smax = 100

    # print(dict_temp)

    # Lấy trị cuối và đầu của dictionary
    rmin = min(dict.keys())
    rmax = max(dict.keys())

    # Tạo một dictionary mới với các giá trị đã được thu hẹp theo công thức
    for key in dict_temp.keys():
        s = dict_temp[key]["s"] = (Smax - Smin)/(rmax - rmin)*(dict_temp[key]["rk"] - rmin) + Smin # Tính giá trị s theo công thức s = (Smax - Smin)/(rmax - rmin)*(rk - rmin) + Smin
        # Làm tròn k'
        if s - int(s) >= 0.5:
            dict_temp[key]['Round(k)'] = int(s) + 1 
        else:
            dict_temp[key]['Round(k)'] = int(s)

     # Duyệt qua dict_temp và nhóm theo Round(k)
    result_dict = {}
    for key, value in dict_temp.items():
        round_k = value['Round(k)']
        nk = value['nk']

        # Nếu Round(k) đã có trong result_dict, cộng thêm nk vào
        if round_k in result_dict:
            result_dict[round_k] += nk  
        else:
            # Nếu chưa có, khởi tạo mới với giá trị nk
            result_dict[round_k] = nk

    # Trả về dictionary đã thu hẹp giá trị
    return result_dict, dict_temp # dict là kết quả sau khi làm tròn k trước khi nhóm theo Round(k), result_dict là kết quả sau khi nhóm theo Round(k)

def ChuyenDoiSangAnhXamCBTH(matrix, dict):
    for i in range(matrix.shape[0]): # Duyệt qua từng hàng
        for j in range(matrix.shape[1]): # Duyệt qua từng cột
                matrix[i][j] = dict[matrix[i][j]]['Round(k)'] # Gán giá trị mới
    return matrix 