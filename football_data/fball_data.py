import csv

#=======================================================================
def ChucNang1():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("1.1 Xem toàn bộ bảng xếp hạng")
        print("1.2 Xem thông tin một đội bóng")
        print("1.3 Tìm đội theo tên")
        print("1.4 Xem top đội ghi bàn nhiều nhất")
        print("1.5 Xem top đội thủng lưới ít nhất")
        print("0 Thoát")
        choice=float(input("Chọn: "))
        if choice==1.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")

        elif choice==1.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")
                elif xacnhan=='N':
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==1.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")
                elif xacnhan=='N':
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==1.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")
                elif xacnhan=='N':
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng nhập lại")
        elif choice==1.5:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")
                elif xacnhan=='N':
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng nhập lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

def ChucNang2():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("2.1 Tổng số trận đã đá")
        print("2.2 Số trận thắng / hòa / thua")
        print("2.3 Hiệu số bàn thắng")
        print("2.4 Điểm trung bình mỗi trận")
        print("2.5 Đánh giá sức mạnh đội bóng")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==2.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==2.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==2.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==2.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==2.5:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

def ChucNang3():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("3.1 Top 4 đội dẫn đầu")
        print("3.2 Top 6 đội tranh cúp châu Âu")
        print("3.3 Nhóm giữa bảng")
        print("3.4 Nhóm nguy cơ xuống hạng")
        print("3.5 Đội có khả năng vô địch")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==3.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==3.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==3.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==3.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==3.5:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

def ChucNang4():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("4.1 Xem chuỗi phong độ từng đội")
        print("4.2 Tính điểm phong độ (W=3, D=1, L=0)")
        print("4.3 Đội có phong độ cao nhất")
        print("4.4 Đội sa sút phong độ")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==4.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang4()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==4.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang4()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==4.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang4()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==4.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang4()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

def ChucNang5():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("5.1 So sánh điểm số")
        print("5.2 So sánh hiệu số bàn thắng")
        print("5.3 So sánh phong độ")
        print("5.4 Đánh giá đội mạnh hơn")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==5.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang5()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==5.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang5()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==5.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang5()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==5.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang5()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

def ChucNang6():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("6.1 Dự đoán thắng / hòa / thua")
        print("6.2 Tính chỉ số sức mạnh (Power Score)")
        print("6.3 Giải thích lý do dự đoán")
        print("6.4 Đánh giá độ tin cậy dự đoán")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==6.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang6()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==6.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang6()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==6.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang6()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==6.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang6()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

def ChucNang7():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("6.1 Dự đoán thắng / hòa / thua")
        print("6.2 Tính chỉ số sức mạnh (Power Score)")
        print("6.3 Giải thích lý do dự đoán")
        print("6.4 Đánh giá độ tin cậy dự đoán")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==6.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang6()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==6.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")
                elif xacnhan=='N':
                    ChucNang6()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==6.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang6()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==6.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang6()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

def ChucNang7():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("7.1 Đội ghi bàn vượt trội")
        print("7.2 Đội thủng lưới bất thường")
        print("7.3 Đội có hiệu suất kém so với điểm số")
        print("7.4 Cảnh báo nguy cơ xuống hạng")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==7.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang7()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==7.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang7()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==7.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang7()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==7.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang7()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

def ChucNang8():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("8.1 Xuất bảng xếp hạng ra file TXT")
        print("8.2 Xuất thống kê đội bóng ra CSV")
        print("8.3 Lưu kết quả dự đoán")
        print("8.4 Tạo báo cáo tổng kết")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==8.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang8()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==8.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang8()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==8.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang8()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==8.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y':
                    print("Xác nhận thành công")

                elif xacnhan=='N':
                    ChucNang8()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

# hàm chính của dự án
with open("dulieu.txt","r",newline="",encoding="UTF-8") as f:
    content=csv.DictReader(f)
    while True:
        print("===== PREMIER LEAGUE ANALYSIS SYSTEM =====")
        print("1.Xem dữ liệu giải đấu")
        print("2. Phân tích đội bóng")
        print("3.Phân tích bảng xếp hạng")
        print("4.Phân tích phong độ (5 trận đấu gần nhất)")
        print("5.So sánh hai đội bóng")
        print("6.Thống kê & phát hiện bất thường")
        print("7.Thống kê & phát hiện bất thường")
        print("8.Báo cáo và xuất dữ liệu")
        print("0.Thoát")
        choice=int(input("Chọn chức năng: "))
        if choice==1:
            ChucNang1()
        elif choice==2:
            ChucNang2()
        elif choice==3:
            ChucNang3()
        elif choice==4:
            ChucNang4()
        elif choice==5:
            ChucNang5()
        elif choice==6:
            ChucNang6()
        elif choice==7:
            ChucNang7()
        elif choice==8:    
            ChucNang8()
        elif choice==0:
            break
        else:
            print("Chọn không đúng giá trị chọn lại")

    