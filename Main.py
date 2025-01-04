import os # Thư viện os để chạy các lệnh trong terminal

def main_menu():
    while True:
        print("\n===== MENU CHỌN BÀI =====")
        print("1. Chạy Bài 1")
        print("2. Chạy Bài 2")
        print("3. Chạy Bài 3")
        print("4. Thoát")

        choice = input("Chọn một lựa chọn: ")

        if choice == '1':
            os.system('python Bai1.py') # Chạy file Bai1.py
        elif choice == '2':
            os.system('python Bai2.py')
        elif choice == '3':
            os.system('python Bai3.py')
        elif choice == '4':
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

if __name__ == '__main__':
    main_menu()