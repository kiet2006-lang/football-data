import csv
def KhungBang():
    print("-"*123)
    print(f"| {'Hạng':<5} | {'Câu lạc bộ':<15} | {'Số trận':<8} | {'Thắng':<6} | {'Hòa':<4} | {'Thua':<5} | {'Bàn thắng':<10} | {'Bàn thua':<10} | {'Hiệu số':<8} | {'5 trận đấu gần nhất':<20} |")
    print("-"*122)

def ToanBoBang():
    with open("football_data/dulieu.txt","r",newline="",encoding="UTF-8") as f:
        content=csv.DictReader(f)
        KhungBang()
        for i in content:
            print(f"| {i['Hạng']:<5} | {i['Câu lạc bộ']:<15} | {i['ST']:<8} | {i['T']:<6} | {i['H']:<4} | {i['T']:<5} | {i['BT']:<10} | {i['BB']:<10} | {i['HS']:<8} | {i['5_tran_gan_nhat']:<20} |")
            print("-"*122)

def ThongTinCuThe1DoiBong():
    try:
        while True:
            print("1.Arsenal")
            print("2.Man City")
            print("3.Aston")
            print("4.Chelsea")
            print("5.Liverpool")
            print("6.Man Utd")
            print("7.Fulham")
            print("8.Everton")
            print("9.Brentford")
            print("10.Newcastle")
            print("11.Sunderland")
            print("12.Bournemouth")
            print("13.Brighton")
            print("14.Tottenham")
            print("15.Crystal Palace")
            print("16.Leeds")
            print("17.Nottm Forest")
            print("18.West Ham")
            print("19.Burnley")
            print("20.Wolves")
            choice=int(input("Chọn: "))
            if choice==1:
                with open("football_data/arsenal.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==2:
                with open("football_data/mancity.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==3:
                with open("football_data/aston.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==4:
                with open("football_data/chelsea.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==5:
                with open("football_data/chelsea.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==6:
                with open("football_data/manutd.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==7:
                with open("football_data/fulham.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==8:
                with open("football_data/everton.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                print("----------------------------------------------------------------------------------------------------")
                for i in content:
                    print(i,end="")
                print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==9:
                with open("football_data/brentford.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==10:
                with open("football_data/newcastle.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                print("----------------------------------------------------------------------------------------------------")
                for i in content:
                    print(i,end="")
                print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==11:
                with open("football_data/sunderland.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==12:
                with open("football_data/bournemouth.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==13:
                with open("football_data/brighton.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==14:
                with open("football_data/tottenham.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==15:
                with open("football_data/crystal_palace.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==16:
                with open("football_data/leeds.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==17:
                with open("football_data/nottm_forest.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==18:
                with open("football_data/west_ham.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==19:
                with open("football_data/burnley.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            elif choice==20:
                with open("football_data/wolves.txt","r",newline="",encoding="UTF-8") as f:
                    content=f.readlines()
                    print("----------------------------------------------------------------------------------------------------")
                    for i in content:
                        print(i,end="")
                    print("----------------------------------------------------------------------------------------------------")
                return
            else:
                print("Nhập kí tự không đúng nhập lạiN!")
    except ValueError:
        print("Phải nhập giá trị số nguyên ! Quay về trang chủ")
        return

def TimDoiTheoTen():
    with open("football_data/dulieu.txt","r",newline="",encoding="UTF-8") as f:
        content=csv.DictReader(f)
        try:
            n=input("Nhập tên đội bóng: ")
            for i in content:                                               
                if n==i["Câu lạc bộ"]:
                    print(f"Câu lạc bộ: {i["Câu lạc bộ"]}")
                    print(f"Số trận: {i['ST']}")
                    print(f"Số trận thắng: {i["T"]}")
                    print(f"Số trận hòa: {i['H']}")
                    print(f"Số trận thua: {i["B"]}")
                    print(f"Số bàn thắng: {i["BT"]}")
                    print(f"Số bàn thua: {i["BB"]}")
                    print(f"Hiệu số: {i["HS"]}")
                    print(f"Điểm: {i["Diem"]}")
                    print(f"5 trận đấu gần nhất: {i["5_tran_gan_nhat"]}")
        except ValueError:
            print("Phải nhập giá trị giá trị chuỗi ! Quay về trang chủ")
            return
        
def XemDoiGhiBanNhieuNhat():
    with open("football_data/dulieu.txt","r",newline="",encoding="UTF-8") as f:
        content=csv.DictReader(f)
        ds=list()
        temp=list()
        for i in content:         # Hạng,Câu lạc bộ,ST,T,H,B,BT,BB,HS,Diem,5_tran_gan_nhat   
            temp.append(i["Hạng"])
            temp.append(i["Câu lạc bộ"])
            temp.append(i["ST"])
            temp.append(i["T"])
            temp.append(i["H"])
            temp.append(i["B"])
            temp.append(i["BT"])
            temp.append(i["BB"])
            temp.append(i["HS"])
            temp.append(i["Diem"])
            temp.append(i["5_tran_gan_nhat"])
            ds.append(temp)
            temp=list()
        lon_nhat=max(ds,key=lambda x:x[6])[6]
        print("===== Các câu lạc bộ ghi bàn nhiều nhất ở Ngoại Hạng Anh =====")
        for i in ds:
            if i[6]==lon_nhat:
                print(f"Tên câu lạc bộ: {i[1]}")
                print(f"Số trận tham gia: {i[2]}")
                print(f"Số trận thắng: {i[3]}")
                print(f"Số trận hòa: {i[4]}")
                print(f"Số trận thua: {i[5]}")
                print(f"Ghi bàn được: {i[6]}")
                print(f"Vào lưới: {i[7]}")
                print(f"Hiệu số: {i[8]}")
                print(f"Điểm: {i[9]}")

def ThungLuoiItNhat():
    with open("football_data/dulieu.txt","r",newline="",encoding="UTF-8") as f:
        content=csv.DictReader(f)                      # Hạng,Câu lạc bộ,ST,T,H,B,BT,BB,HS,Diem,5_tran_gan_nhat 
        ds=list()
        temp=list()
        for i in content:
            temp.append(i["Hạng"])
            temp.append(i["Câu lạc bộ"])
            temp.append(i["ST"])
            temp.append(i["T"])
            temp.append(i["H"])
            temp.append(i["B"])
            temp.append(i["BT"])
            temp.append(i["BB"])
            temp.append(i["HS"])
            temp.append(i["Diem"])
            temp.append(i["5_tran_gan_nhat"])
            ds.append(temp)
            temp=list()
        nho_nhat=min(ds,key=lambda x:x[7])[7]
        print("===== Các câu lạc bộ thủng lưới ít nhất ở Ngoại Hạng Anh =====")
        for i in ds:
            if i[7]==nho_nhat:
                print(f"Tên câu lạc bộ: {i[1]}")
                print(f"Số trận tham gia: {i[2]}")
                print(f"Số trận thắng: {i[3]}")
                print(f"Số trận hòa: {i[4]}")
                print(f"Số trận thua: {i[5]}")
                print(f"Ghi bàn đượcL {i[6]}")
                print(f"Vào lưới: {i[7]}")
                print(f"Hiệu số: {i[8]}")
                print(f"Điểm: {i[9]}")
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
                if xacnhan=='Y' or xacnhan=="y":
                    print("Xác nhận thành công")
                    print()
                    ToanBoBang()
                    return
                elif xacnhan=='N' or xacnhan=="n":
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")

        elif choice==1.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=="y":
                    print("Xác nhận thành công")
                    ThongTinCuThe1DoiBong()
                    return
                elif xacnhan=='N' or xacnhan=="n":
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==1.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' and xacnhan=="y":
                    print("Xác nhận thành công")
                    TimDoiTheoTen()
                    return
                elif xacnhan=='N' or xacnhan=="n":
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==1.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    XemDoiGhiBanNhieuNhat()
                    return
                elif xacnhan=='N' or xacnhan=="n":
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng nhập lại")
        elif choice==1.5:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    ThungLuoiItNhat()
                    return
                elif xacnhan=='N' or xacnhan=="n":
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng nhập lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")

#==================================================================================================================
def TongSoTranDa():
    with open("football_data/dulieu.txt","r",newline="",encoding="UTF-8") as f:
        content=csv.DictReader(f)
        tong=0
        for i in content:
            tong+=int(i["ST"])
    print(f"Số trận đã đá tại mùa 2025-2026 là: {tong} trận")

def TongSoTranThang_Hoa_Thua():
    with open("football_data/dulieu.txt","r",newline="",encoding="UTF-8") as f:
        content=csv.DictReader(f)
        tong_thang=0
        tong_hoa=0
        tong_thua=0
        for i in content:
            tong_thang+=int(i["T"])
            tong_hoa+=int(i["H"])
            tong_thua+=int(i['T'])
        print(f"Tổng số trận thắng là: {tong_thang} trận")
        print(f"Tổng số trận hòa là: {tong_hoa} trận")
        print(f"Tổng số trận thua là: {tong_thua} trận")

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
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    TongSoTranDa()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==2.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    TongSoTranThang_Hoa_Thua()
                    return
                elif xacnhan=='N' or xacnhan=='n':
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
def main():
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

#============================================================================
main()
    