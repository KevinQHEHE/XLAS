import numpy as np
from AnhXam import ChuyenDoiAnhSangAnhXam, ChuyenDoiAnhXamSangMaTran, ChuyenDoiMaTranSangAnhXam
from XuLyHisto import VeHistogram, VeHistogramSauCanBang, CanBangHisto, ThuHep, ChuyenDoiSangAnhXamCBTH
from PIL import Image
import matplotlib.pyplot as plt

# Main
if __name__ == '__main__':
    array_img = None
    # Menu chọn ảnh từ 1 đến 10
    print("Chọn ảnh từ 1 đến 10:")
    for i in range(1, 11):
        print(f"{i}. anh{i}.jpg")
    
    choice = int(input("Nhập số của ảnh bạn muốn chọn: "))
    if 1 <= choice <= 10:
        image = f"anh{choice}.jpg"
        imageGray = ChuyenDoiAnhSangAnhXam(image) # Chuyển ảnh màu sang ảnh xám, trả về một mảng NumPy đại diện cho dữ liệu ảnh xám.
        Image.fromarray(ChuyenDoiAnhSangAnhXam(image)).show() # Hiện ảnh xám để so sánh với ảnh gốc, sử dụng Image.fromarray để chuyển mảng NumPy thành ảnh.
        array_img = ChuyenDoiAnhXamSangMaTran(imageGray) # Chuyển ảnh xám sang ma trận
        # print(array_img) # In ma trận ảnh xám
    else:
        print("Lựa chọn không hợp lệ. Sử dụng ảnh mặc định.")  

    # data = array_img.flatten() # Chuyển ma trận thành mảng 1 chiều, sử dụng cho việc vẽ histogram của ảnh gốc
    # data = sorted(data) # Sắp xếp mảng theo thứ tự tăng dần  

    # Vẽ histogram của hình ảnh
    VeHistogram(array_img, "Histogram của I")
    
    a, b = CanBangHisto(array_img) # a là kết quả cân bằng, b là kết quả trước khi nhóm k, trước khi làm tròn k 
    
    # Vẽ histogram của hình ảnh sau khi cân bằng
    VeHistogramSauCanBang(a, "Histogram của H2") 
    c = ChuyenDoiSangAnhXamCBTH(array_img, b) # c là ma trận ảnh sau khi cân bằng histogram
    ChuyenDoiMaTranSangAnhXam(c).show() # hiện ảnh sau khi cân bằng histogram

    d, e = ThuHep(a) # d là kết quả thu hẹp, e là kết quả trước khi nhóm k, trước khi làm tròn k của thu hẹp

    f = ChuyenDoiSangAnhXamCBTH(c, e) # f là ma trận ảnh sau khi thu hẹp histogram

    ChuyenDoiMaTranSangAnhXam(f).show()# hiện ảnh sau khi thu hẹp histogram
    VeHistogramSauCanBang(d, "Histogram của H2 sau khi thu hẹp")




    # # Tạo một dictionary để lưu trữ giá trị và số lần xuất hiện
    # dict = {}
    # # Duyệt qua từng giá trị trong mảng
    # for pixel in data:
    #     if pixel in dict:
    #         dict[pixel] += 1  # Tăng tần suất nếu giá trị đã tồn tại
    #     else:
    #         dict[pixel] = 1  # Khởi tạo giá trị tần suất ban đầu là 1

    # # print(dict)
    # x, y = ThuHep(dict) # can bang histogram cho anh goc

    # z = ChuyenDoiSangAnhXamCBTH(array_img, y) # z la ma tran anh sau khi can bang histogram cho anh goc

    # ChuyenDoiMaTranSangAnhXam(z).show() # hien anh sau khi can bang histogram cho anh goc
    # VeHistogramSauCanBang(x, "Histogram của ảnh gốc sau khi thu hẹp")


    # fig, axs = plt.subplots(1, 4, figsize=(12, 6))
    # axs[3].hist(np.array(list(x.keys())).ravel(), bins=256, color='purple', alpha=0.9, weights=np.array(list(x.values())).ravel()) # list(x.keys()) là list các giá trị, ravel() làm phẳng mảng, bins=256 là số lượng bins, color là màu sắc, alpha là độ trong suốt, weights là trọng số
    # axs[3].set_title('Histogram thu hẹp của ảnh gốc')
   
    # axs[2].hist(np.array(list(d.keys())).ravel(), bins=256, color='red', alpha=0.9, weights=np.array(list(d.values())).ravel())
    # axs[2].set_title('Histogram thu hẹp sau khi cân bằng')

    # axs[1].hist(np.array(list(a.keys())).ravel(), bins=256, color='green', alpha=0.9, weights=np.array(list(a.values())).ravel())
    # axs[1].set_title('Histogram cân bằng của ảnh gốc')
    
    # axs[0].set_title('Histogram của Ảnh gốc')
    # axs[0].hist(data, bins=256, color='blue', alpha=0.9)
    # plt.show()

    fig, axs = plt.subplots(2, 4, figsize=(16, 8))

    # Hiển thị ảnh
    axs[0, 0].imshow(imageGray, cmap='gray')
    axs[0, 0].set_title("Ảnh gốc")
    axs[0, 0].axis('off')

    axs[0, 1].imshow(ChuyenDoiMaTranSangAnhXam(c), cmap='gray')
    axs[0, 1].set_title("Ảnh cân bằng histogram")
    axs[0, 1].axis('off')

    axs[0, 2].imshow(ChuyenDoiMaTranSangAnhXam(f), cmap='gray')
    axs[0, 2].set_title("Ảnh thu hẹp sau khi cân bằng histogram")
    axs[0, 2].axis('off') # Tắt trục

    # axs[0, 3].imshow(ChuyenDoiMaTranSangAnhXam(z), cmap='gray')
    # axs[0, 3].set_title("Ảnh sau thu hẹp ảnh gốc")
    # axs[0, 3].axis('off')

    # Hiển thị histogram
    # axs[1, 0].hist(data, bins=256, color='blue', alpha=0.9)
    # axs[1, 0].set_title("Histogram của Ảnh gốc")

    axs[1, 1].hist(np.array(list(a.keys())).ravel(), bins=256, color='green', alpha=0.9, weights=np.array(list(a.values())).ravel())
    axs[1, 1].set_title("Histogram cân bằng của ảnh gốc")

    axs[1, 2].hist(np.array(list(d.keys())).ravel(), bins=256, color='red', alpha=0.9, weights=np.array(list(d.values())).ravel())
    axs[1, 2].set_title("Histogram thu hẹp sau khi cân bằng")

    # axs[1, 3].hist(np.array(list(x.keys())).ravel(), bins=256, color='purple', alpha=0.9, weights=np.array(list(x.values())).ravel())
    # axs[1, 3].set_title("Histogram thu hẹp của ảnh gốc")

    # Hiển thị tất cả
    plt.tight_layout()
    plt.show()