import os
import sys
import csv

def ChucNang1():
    print("Chọn chức năng chi tiết hơn")
    print("1.1.Xem toàn bộ bảng xếp hạng")
    print("1.2.Xem thông tin một đội bóng")
    print("1.3.Tìm đội theo tên")
    print("1.4.Xem top đội ghi bàn nhiều nhất")
    print("1.5.Xem top đội thủng lưới ít nhất")
    choice=float(input("Chọn: "))
    if choice==1.1:
        while True:
            xacnhan=input("Xác nhận Y/N: ")
            if xacnhan=='Y':
                print("Xác nhận thanh công")
            elif xacnhan=='N':
                ChucNang1()
            else:
                print("Nhập không phải Y hay N! Vui lòng nhập lại")

    elif choice==1.2:
        xacnhan=input("")
    elif choice    

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
        print("7.Báo cáo và xuất dữ liệu")
        print("0.Thoát")
        choice=int(input("Chọn chức năng: "))
        if choice==1:

        elif choice==2:

        elif choice==3:

        elif choice==4:
        
        elif choice==5:

        elif choice==6:

        elif choice==7:
        
        elif choie==0:
            break
        else:
            print("Chọn không đúng giá trị chọn lại")

    