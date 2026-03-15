import csv
import os

# Load dulieu.txt once from disk and reuse the in-memory list throughout the
# program, instead of opening the file on every individual function call.
_DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dulieu.txt")
_DATA_CACHE = None


def _load_data():
    """Return the league data rows, reading from disk only on the first call."""
    global _DATA_CACHE
    if _DATA_CACHE is None:
        with open(_DATA_FILE, "r", newline="", encoding="UTF-8") as f:
            _DATA_CACHE = list(csv.DictReader(f))
    return _DATA_CACHE


# Single source of truth for team names (must match the CSV exactly).
_TEAMS = [
    "Arsenal", "Man City", "Aston Villa", "Man Utd", "Chelsea",
    "Liverpool", "Brentford", "Bournemouth", "Everton", "Fulham",
    "Newcastle", "Sunderland", "Crystal Palace", "Brighton", "Leeds",
    "Tottenham", "Nottm Forest", "West Ham", "Burnley", "Wolves",
]

# Map menu number to club overview filename (for feature 1.2)
_CLUB_FILES = {
    1: "arsenal", 2: "mancity", 3: "aston", 4: "manutd", 5: "chelsea",
    6: "liverpool", 7: "brentford", 8: "bournemouth", 9: "everton", 10: "fulham",
    11: "newcastle", 12: "sunderland", 13: "crystal_palace", 14: "brighton",
    15: "leeds", 16: "tottenham", 17: "nottm_forest", 18: "west_ham",
    19: "burnley", 20: "wolves",
}


def _hien_thi_menu_doi():
    """Print the numbered team selection menu."""
    for idx, name in enumerate(_TEAMS, 1):
        print(f"{idx}.{name}")


def _chon_doi(prompt):
    """Display the team menu, read a choice and return the team name.

    Raises ValueError if the user enters a non-integer (propagates to the
    caller's except-block, consistent with the original error handling).
    """
    while True:
        _hien_thi_menu_doi()
        choice = int(input(prompt))
        if 1 <= choice <= len(_TEAMS):
            return _TEAMS[choice - 1]
        print("Nhập kí tự không đúng nhập lại!")


def _tinh_diem_phong_do(form_str):
    """Return the form-score for a 5-match result string (W=3, D=1, L=0)."""
    return sum(3 if c == 'W' else 1 if c == 'D' else 0 for c in form_str)


def _tinh_chuoi_thang(form_str):
    """Return the longest consecutive win streak in the form string."""
    best = cur = 0
    for ch in form_str:
        if ch == 'W':
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return best


def _lay_du_lieu_va_tinh_power_score(a, b):
    """Fetch rows for teams a and b and compute their PowerScores.

    Returns (tt1, tt2, ps1, ps2, res1, res2) where tt_x is
    [name, diem, hieu_so, form_str] and res_x is the win streak.
    """
    content = _load_data()
    tt1 = tt2 = None
    for row in content:
        name = row['Câu lạc bộ']
        if name == a:
            tt1 = [name, row['Diem'], row['HS'], row['5_tran_gan_nhat']]
        elif name == b:
            tt2 = [name, row['Diem'], row['HS'], row['5_tran_gan_nhat']]
        if tt1 and tt2:
            break
    res1 = _tinh_chuoi_thang(tt1[3])
    res2 = _tinh_chuoi_thang(tt2[3])
    ps1 = int(tt1[1]) + int(tt1[2]) * 0.5 + res1 * 10
    ps2 = int(tt2[1]) + int(tt2[2]) * 0.5 + res2 * 10
    return tt1, tt2, ps1, ps2, res1, res2


#=======================================================================
def KhungBang():
    print("-"*122)
    print(f"| {'Hạng':<5} | {'Câu lạc bộ':<15} | {'Số trận':<8} | {'Thắng':<6} | {'Hòa':<4} | {'Thua':<5} | {'Bàn thắng':<10} | {'Bàn thua':<10} | {'Hiệu số':<8} | {'5 trận đấu gần nhất':<20} |")
    print("-"*122)


def ToanBoBang():
    content = _load_data()
    KhungBang()
    for i in content:
        print(f"| {i['Hạng']:<5} | {i['Câu lạc bộ']:<15} | {i['ST']:<8} | {i['T']:<6} | {i['H']:<4} | {i['B']:<5} | {i['BT']:<10} | {i['BB']:<10} | {i['HS']:<8} | {i['5_tran_gan_nhat']:<20} |")
        print("-"*122)


def ThongTinCuThe1DoiBong():
    try:
        while True:
            _hien_thi_menu_doi()
            choice = int(input("Chọn: "))
            if choice in _CLUB_FILES:
                filepath = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    "tongquanclb",
                    f"{_CLUB_FILES[choice]}.txt",
                )
                with open(filepath, "r", newline="", encoding="UTF-8") as f:
                    content = f.readlines()
                print("-"*100)
                for line in content:
                    print(line, end="")
                print("-"*100)
                return
            else:
                print("Nhập kí tự không đúng nhập lại!")
    except ValueError:
        print("Phải nhập giá trị số nguyên ! Quay về trang chủ")
        return


def TimDoiTheoTen():
    content = _load_data()
    try:
        n = input("Nhập tên đội bóng: ")
        for i in content:
            if n == i["Câu lạc bộ"]:
                print(f"Câu lạc bộ: {i['Câu lạc bộ']}")
                print(f"Số trận: {i['ST']}")
                print(f"Số trận thắng: {i['T']}")
                print(f"Số trận hòa: {i['H']}")
                print(f"Số trận thua: {i['B']}")
                print(f"Số bàn thắng: {i['BT']}")
                print(f"Số bàn thua: {i['BB']}")
                print(f"Hiệu số: {i['HS']}")
                print(f"Điểm: {i['Diem']}")
                print(f"5 trận đấu gần nhất: {i['5_tran_gan_nhat']}")
    except ValueError:
        print("Phải nhập giá trị giá trị chuỗi ! Quay về trang chủ")
        return


def XemDoiGhiBanNhieuNhat():
    content = _load_data()
    lon_nhat = max(content, key=lambda x: int(x['BT']))['BT']
    print("===== Các câu lạc bộ ghi bàn nhiều nhất ở Ngoại Hạng Anh =====")
    for i in content:
        if i['BT'] == lon_nhat:
            print(f"Tên câu lạc bộ: {i['Câu lạc bộ']}")
            print(f"Số trận tham gia: {i['ST']}")
            print(f"Số trận thắng: {i['T']}")
            print(f"Số trận hòa: {i['H']}")
            print(f"Số trận thua: {i['B']}")
            print(f"Ghi bàn được: {i['BT']}")
            print(f"Vào lưới: {i['BB']}")
            print(f"Hiệu số: {i['HS']}")
            print(f"Điểm: {i['Diem']}")


def ThungLuoiItNhat():
    content = _load_data()
    nho_nhat = min(content, key=lambda x: int(x['BB']))['BB']
    print("===== Các câu lạc bộ thủng lưới ít nhất ở Ngoại Hạng Anh =====")
    for i in content:
        if i['BB'] == nho_nhat:
            print(f"Tên câu lạc bộ: {i['Câu lạc bộ']}")
            print(f"Số trận tham gia: {i['ST']}")
            print(f"Số trận thắng: {i['T']}")
            print(f"Số trận hòa: {i['H']}")
            print(f"Số trận thua: {i['B']}")
            print(f"Ghi bàn được: {i['BT']}")
            print(f"Vào lưới: {i['BB']}")
            print(f"Hiệu số: {i['HS']}")
            print(f"Điểm: {i['Diem']}")


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
                    print()
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
                    print()
                    print()
                    print()
                    ThongTinCuThe1DoiBong()
                    return
                elif xacnhan=='N' or xacnhan=="n":
                    ChucNang1()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==1.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
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
                    print()
                    print()
                    print()
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
                    print()
                    print()
                    print()
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


#=======================================================================
def TongSoTranDa():
    content = _load_data()
    tong = sum(int(i["ST"]) for i in content)
    print(f"Số trận đã đá tại mùa 2025-2026 là: {tong} trận")


def TongSoTranThang_Hoa_Thua():
    content = _load_data()
    tong_thang = sum(int(i["T"]) for i in content)
    tong_hoa   = sum(int(i["H"]) for i in content)
    tong_thua  = sum(int(i["B"]) for i in content)
    print(f"Tổng số trận thắng là: {tong_thang} trận")
    print(f"Tổng số trận hòa là: {tong_hoa} trận")
    print(f"Tổng số trận thua là: {tong_thua} trận")


def HieuSoBanThang():
    content = _load_data()
    print("===== BẢNG HIỆU SỐ CỦA CÁC CÂU LẠC BỘ NGOẠI HẠNG ANH =====")
    for i in content:
        if i['HS'][0]=='-':
            print(f"{i['Câu lạc bộ']:<15} : {i['HS']:<4}")
        else:
            print(f"{i['Câu lạc bộ']:<15} : +{i['HS']:<3}")


def DiemTrungBinhMoiTran():
    content = _load_data()
    print("===== BẢNG TRUNG BÌNH MỖI TRẬN CỦA CÁC CÂU LẠC BỘ NGOẠI HẠNG ANH =====")
    print()
    print("-"*48)
    print(f"| {'Câu lạc bộ':<15} | {'Điểm trung bình mỗi trận':<25} |")
    print("-"*48)
    for i in content:
        print(f"| {i['Câu lạc bộ']:<15} | {str(round(float(i['Diem'])/float(i['ST']),2)):<25} |")
        print("-"*48)


def DanhGiaTungDoiBong():
    content = _load_data()
    print("===== BẢNG ĐÁNH GIÁ TỪNG ĐỘI BÓNG =====")
    print()
    print("-"*40)
    print(f"| {'Câu lạc bộ':<15} | {'Đánh giá':<20} |")
    print("-"*40)
    for i in content:
        ppg = float(i['Diem']) / float(i['ST'])
        hs  = float(i['HS'])
        if ppg > 1.5 and hs > 0:
            danh_gia = "Đội bóng mạnh"
        elif ppg > 1 and hs > 0:
            danh_gia = "Đội bóng khá"
        elif ppg < 0.5 and hs < 0:
            danh_gia = "Đội bóng yếu"
        else:
            danh_gia = "Đội bóng tầm trung"
        print(f"| {i['Câu lạc bộ']:<15} | {danh_gia:<20} |")
        print("-"*40)


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
                    print()
                    print()
                    print()
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
                    print()
                    print()
                    print()
                    TongSoTranThang_Hoa_Thua()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==2.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    HieuSoBanThang()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==2.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    DiemTrungBinhMoiTran()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==2.5:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    DanhGiaTungDoiBong()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang2()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")


#=======================================================================
def _in_bang(rows):
    """Print a formatted standings table for the given subset of rows."""
    print("-"*122)
    print(f"| {'Top':<5} | {'Câu lạc bộ':<15} | {'Số trận':<8} | {'Thắng':<6} | {'Hòa':<4} | {'Thua':<5} | {'Bàn thắng':<10} | {'Bàn thua':<10} | {'Hiệu số':<8} | {'5 trận đấu gần nhất':<20} |")
    print("-"*122)
    for cnt, i in enumerate(rows, 1):
        print(f"| {cnt:<5} | {i['Câu lạc bộ']:<15} | {i['ST']:<8} | {i['T']:<6} | {i['H']:<4} | {i['B']:<5} | {i['BT']:<10} | {i['BB']:<10} | {i['HS']:<8} | {i['5_tran_gan_nhat']:<20} |")
        print("-"*122)


def Top4():
    content = _load_data()
    print(" "*35+"===== TOP 4 CÂU LẠC BỘ NGOẠI HẠNG ANH =====")
    _in_bang(content[:4])
    print()


def Top6():
    content = _load_data()
    print(" "*25+"===== TOP 6 CÂU LẠC BỘ NGOẠI HẠNG ANH TRANH CÚP CHÂU ÂU =====")
    _in_bang(content[:6])


def GiuaBang():
    content = _load_data()
    print(" "*25+"===== NHÓM GIỮA BẢNG CỦA CÂU LẠC BỘ NGOẠI HẠNG ANH TRANH CÚP CHÂU ÂU =====")
    _in_bang(content[7:15])


def TruHang():
    content = _load_data()
    print(" "*25+"===== NHÓM TRỤ HẠNG CÂU LẠC BỘ NGOẠI HẠNG ANH TRANH CÚP CHÂU ÂU =====")
    _in_bang(content[15:])


def DuDoanDoiVoDich():
    content = _load_data()
    sorted_hs  = sorted(content, key=lambda x: int(x['HS']), reverse=True)
    sorted_ppg = sorted(content, key=lambda x: float(x['Diem']) / float(x['ST']), reverse=True)
    n = len(content)
    score_hs  = {row['Câu lạc bộ']: n - idx for idx, row in enumerate(sorted_hs)}
    score_ppg = {row['Câu lạc bộ']: n - idx for idx, row in enumerate(sorted_ppg)}
    combined  = {name: score_hs[name] + score_ppg[name] for name in score_hs}
    top4 = sorted(combined, key=combined.get, reverse=True)[:4]
    print(f"4 đội có khả năng vô địch: {top4[0]},{top4[1]},{top4[2]},{top4[3]}")


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
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    Top4()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==3.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    Top6()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==3.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    GiuaBang()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==3.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    TruHang()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==3.5:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    DuDoanDoiVoDich()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang3()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")


#=======================================================================
def ChuoiPhongDoTungDoi():
    content = _load_data()
    print("-"*37)
    print(f"| {'Tên đội bóng':<15} | {'Chuỗi phong độ':<15} |")
    print("-"*37)
    for i in content:
        print(f"| {i['Câu lạc bộ']:<15} | {i['5_tran_gan_nhat']:<15} |")
        print("-"*37)


def TinhDiemPhongDo():
    content = _load_data()
    print("-"*37)
    print(f"| {'Tên đội bóng':<15} | {'Điểm phong độ':<15} |")
    print("-"*37)
    for i in content:
        score = _tinh_diem_phong_do(i['5_tran_gan_nhat'])
        print(f"| {i['Câu lạc bộ']:<15} | {score:<15} |")
        print("-"*37)


def PhongDoCaoNhat():
    content = _load_data()
    ds = [[i['Câu lạc bộ'], _tinh_diem_phong_do(i['5_tran_gan_nhat'])] for i in content]
    # Compute the maximum once, outside the loop, to avoid O(n^2) behaviour.
    cao_nhat = max(ds, key=lambda x: x[1])[1]
    print("Đội bóng có phong độ cao nhất là:")
    for i in ds:
        if i[1] == cao_nhat:
            print(f"{i[0]}")


def PhongDoThapNhat():
    content = _load_data()
    ds = [[i['Câu lạc bộ'], _tinh_diem_phong_do(i['5_tran_gan_nhat'])] for i in content]
    # Compute the minimum once, outside the loop, to avoid O(n^2) behaviour.
    thap_nhat = min(ds, key=lambda x: x[1])[1]
    print("Đội bóng có phong độ thấp nhất là:")
    for i in ds:
        if i[1] == thap_nhat:
            print(f"{i[0]}")


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
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    ChuoiPhongDoTungDoi()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang4()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==4.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    TinhDiemPhongDo()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang4()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==4.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    PhongDoCaoNhat()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang4()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==4.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    PhongDoThapNhat()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang4()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")


#=======================================================================
lssosanh=[]


def SoSanhDiemSoHaiDoi():
    try:
        thu_nhat = _chon_doi("Chọn đội định so sánh thứ nhất: ")
        thu_hai  = _chon_doi("Chọn đội định so sánh thứ hai: ")
        if thu_nhat == thu_hai:
            print("Chọn hai đội trùng nhau!")
            return
        content = _load_data()
        tt1 = tt2 = None
        for i in content:
            if i["Câu lạc bộ"] == thu_nhat:
                tt1 = i
            elif i["Câu lạc bộ"] == thu_hai:
                tt2 = i
            if tt1 and tt2:
                break
        kq = (
            f"Câu lạc bộ thứ nhất: {tt1['Câu lạc bộ']}\n"
            f"Điểm: {tt1['Diem']}\n"
            f"Câu lạc bộ thứ 2: {tt2['Câu lạc bộ']}\n"
            f"Điểm: {tt2['Diem']}\n"
        )
        if int(tt1['Diem']) > int(tt2['Diem']):
            kq += f"Câu lạc bộ {tt1['Câu lạc bộ']} nhiều điểm hơn {tt2['Câu lạc bộ']}\n"
        elif int(tt1['Diem']) < int(tt2['Diem']):
            kq += f"Câu lạc bộ {tt2['Câu lạc bộ']} nhiều điểm hơn {tt1['Câu lạc bộ']}\n"
        else:
            kq += "Hai câu lạc bộ có số điểm bằng nhau\n"
        print(kq)
        lssosanh.append(kq)
    except ValueError:
        print("Phải nhập giá trị số nguyên ! Quay về trang chủ")
        return


def SoSanhHieuSoBanThang():
    try:
        thu_nhat = _chon_doi("Chọn đội định so sánh thứ nhất: ")
        thu_hai  = _chon_doi("Chọn đội định so sánh thứ hai: ")
        if thu_nhat == thu_hai:
            print("Chọn hai đội trùng nhau!")
            return
        content = _load_data()
        tt1 = tt2 = None
        for i in content:
            if i["Câu lạc bộ"] == thu_nhat:
                tt1 = i
            elif i["Câu lạc bộ"] == thu_hai:
                tt2 = i
            if tt1 and tt2:
                break
        kq = (
            f"Câu lạc bộ thứ nhất: {tt1['Câu lạc bộ']}\n"
            f"Hiệu số bàn thắng: {tt1['BT']}\n"
            f"Câu lạc bộ thứ 2: {tt2['Câu lạc bộ']}\n"
            f"Hiệu số bàn thắng: {tt2['BT']}\n"
        )
        if int(tt1['BT']) > int(tt2['BT']):
            kq += f"Câu lạc bộ {tt1['Câu lạc bộ']} có hiệu số bàn thắng lớn hơn {tt2['Câu lạc bộ']}\n"
        elif int(tt1['BT']) < int(tt2['BT']):
            kq += f"Câu lạc bộ {tt2['Câu lạc bộ']} có hiệu số bàn thắng lớn hơn {tt1['Câu lạc bộ']}\n"
        else:
            kq += "Hai câu lạc bộ có hiệu số bàn thắng bằng nhau\n"
        print(kq)
        lssosanh.append(kq)
    except ValueError:
        print("Phải nhập giá trị số nguyên ! Quay về trang chủ")
        return


def SoSanhPhongDo():
    try:
        thu_nhat = _chon_doi("Chọn đội định so sánh thứ nhất: ")
        thu_hai  = _chon_doi("Chọn đội định so sánh thứ hai: ")
        if thu_nhat == thu_hai:
            print("Chọn hai đội trùng nhau!")
            return
        content = _load_data()
        tt1 = tt2 = None
        for i in content:
            # Each team's form score is calculated independently (no shared accumulator).
            if i["Câu lạc bộ"] == thu_nhat:
                tt1 = [i["Câu lạc bộ"], _tinh_diem_phong_do(i["5_tran_gan_nhat"])]
            elif i["Câu lạc bộ"] == thu_hai:
                tt2 = [i["Câu lạc bộ"], _tinh_diem_phong_do(i["5_tran_gan_nhat"])]
            if tt1 and tt2:
                break
        kq = (
            f"Câu lạc bộ thứ nhất: {tt1[0]}\n"
            f"Điểm phong độ: {tt1[1]}\n"
            f"Câu lạc bộ thứ 2: {tt2[0]}\n"
            f"Điểm phong độ: {tt2[1]}\n"
        )
        if tt1[1] > tt2[1]:
            kq += f"Câu lạc bộ {tt1[0]} có phong độ tốt hơn {tt2[0]}\n"
        elif tt1[1] < tt2[1]:
            kq += f"Câu lạc bộ {tt2[0]} có phong độ tốt hơn {tt1[0]}\n"
        else:
            kq += "Hai câu lạc bộ có phong độ bằng nhau\n"
        print(kq)
        lssosanh.append(kq)
    except ValueError:
        print("Phải nhập giá trị số nguyên ! Quay về trang chủ")
        return


def DanhGiaDoiManhHon():
    try:
        thu_nhat = _chon_doi("Chọn đội định so sánh thứ nhất: ")
        thu_hai  = _chon_doi("Chọn đội định so sánh thứ hai: ")
        if thu_nhat == thu_hai:
            print("Chọn hai đội trùng nhau!")
            return
        content = _load_data()
        tt1 = tt2 = None
        for i in content:
            if i["Câu lạc bộ"] == thu_nhat:
                tt1 = [i["Câu lạc bộ"], i['Diem'], i['BT'], _tinh_diem_phong_do(i["5_tran_gan_nhat"])]
            elif i["Câu lạc bộ"] == thu_hai:
                tt2 = [i["Câu lạc bộ"], i['Diem'], i['BT'], _tinh_diem_phong_do(i["5_tran_gan_nhat"])]
            if tt1 and tt2:
                break
        danhgia1 = danhgia2 = 0
        kq = (
            f"Câu lạc bộ thứ nhất: {tt1[0]}\n"
            f"Điểm: {tt1[1]}\n"
            f"Hiệu số bàn thắng: {tt1[2]}\n"
            f"Điểm phong độ: {tt1[3]}\n"
            f"Câu lạc bộ thứ 2: {tt2[0]}\n"
            f"Điểm: {tt2[1]}\n"
            f"Hiệu số bàn thắng: {tt2[2]}\n"
            f"Điểm phong độ: {tt2[3]}\n"
        )
        if int(tt1[1]) > int(tt2[1]):
            danhgia1 += 1
        elif int(tt1[1]) < int(tt2[1]):
            danhgia2 += 1
        if int(tt1[2]) > int(tt2[2]):
            danhgia1 += 1
        elif int(tt1[2]) < int(tt2[2]):
            danhgia2 += 1
        if tt1[3] > tt2[3]:
            danhgia1 += 1
        elif tt1[3] < tt2[3]:
            danhgia2 += 1
        if danhgia1 > danhgia2:
            kq += f"{tt1[0]} mạnh hơn {tt2[0]}\n"
        elif danhgia1 < danhgia2:
            kq += f"{tt2[0]} mạnh hơn {tt1[0]}\n"
        print(kq)
        lssosanh.append(kq)
    except ValueError:
        print("Phải nhập giá trị số nguyên ! Quay về trang chủ")
        return


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
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    SoSanhDiemSoHaiDoi()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang5()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==5.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    SoSanhHieuSoBanThang()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang5()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==5.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    SoSanhPhongDo()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang5()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==5.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    DanhGiaDoiManhHon()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang5()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")


#=======================================================================
lsdudoan=[]


def DuDoanThangHoaThua(a, b):
    tt1, tt2, ps1, ps2, _r1, _r2 = _lay_du_lieu_va_tinh_power_score(a, b)
    if ps1 > ps2:
        kq = f"Câu lạc bộ {a} sẽ thắng câu lạc bộ {b}"
    elif ps1 < ps2:
        kq = f"Câu lạc bộ {a} sẽ thua câu lạc bộ {b}"
    else:
        kq = f"Câu lạc bộ {a} sẽ hòa câu lạc bộ {b}"
    print(kq)
    return kq


def TinhChiSoPowerScore(a, b):
    tt1, tt2, ps1, ps2, _r1, _r2 = _lay_du_lieu_va_tinh_power_score(a, b)
    kq = f"PowerScore của câu lạc bộ {a} là: {ps1}\n" + f"PowerScore của câu lạc bộ {b} là {ps2}\n"
    print(kq)
    return kq


def GiaiThichLyDo(a, b):
    tt1, tt2, ps1, ps2, res1, res2 = _lay_du_lieu_va_tinh_power_score(a, b)
    if ps1 > ps2:
        kq = f"Câu lạc bộ {a} được dự đoán thắng vì: "
        if int(tt1[1]) > int(tt2[1]):
            kq += f"\nCó điểm cao hơn: ({tt1[1]}>{tt2[1]})"
        if int(tt1[2]) > int(tt2[2]):
            kq += f"\nCó hiệu số cao hơn: ({tt1[2]}>{tt2[2]})"
        if res1 > res2:
            kq += f"\nCó chuỗi thắng gần đây là: {res1}"
    elif ps1 < ps2:
        kq = f"Câu lạc bộ {b} được dự đoán thắng vì: "
        if int(tt1[1]) < int(tt2[1]):
            kq += f"\nCó điểm cao hơn: ({tt2[1]}>{tt1[1]})"
        if int(tt1[2]) < int(tt2[2]):
            kq += f"\nCó hiệu số cao hơn: ({tt2[2]}>{tt1[2]})"
        if res1 < res2:
            kq += f"\nCó chuỗi thắng gần đây là: {res2}"
    else:
        kq = f"Câu lạc bộ {a} và {b} được dự đoán hòa vì: "
        kq += "\nPowerScore của 2 câu lạc bộ bằng nhau"
    print(kq)
    return kq


def DoUyTinDuDoan(a, b):
    tt1, tt2, ps1, ps2, _r1, _r2 = _lay_du_lieu_va_tinh_power_score(a, b)
    diff = abs(ps1 - ps2)
    if diff < 3:
        kq = "Độ tin cậy thấp chưa thể chính xác"
    elif diff <= 5:
        kq = "Độ tin cậy trung bình có thể tham khảo"
    else:
        kq = "Độ tin cậy cao có thể tin"
    print(kq)
    return kq


def ChucNang6():
    try:
        thu_nhat = _chon_doi("Chọn đội định so sánh thứ nhất: ")
        thu_hai  = _chon_doi("Chọn đội định so sánh thứ hai: ")
        if thu_nhat == thu_hai:
            print("Chọn hai đội trùng nhau!")
            return
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
                    if xacnhan=='Y' or xacnhan=='y':
                        print("Xác nhận thành công")
                        print()
                        print()
                        print()
                        kq=DuDoanThangHoaThua(thu_nhat,thu_hai)
                        lsdudoan.append([thu_nhat,thu_hai,kq])
                        return
                    elif xacnhan=='N' or xacnhan=='n':
                        ChucNang6()
                    else:
                        print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
            elif choice==6.2:
                while True:
                    xacnhan=input("Xác nhận (Y/N): ")
                    if xacnhan=='Y' or xacnhan=='y':
                        print("Xác nhận thành công")
                        print()
                        print()
                        print()
                        kq=TinhChiSoPowerScore(thu_nhat,thu_hai)
                        lsdudoan.append([thu_nhat,thu_hai,kq])
                        return
                    elif xacnhan=='N' or xacnhan=='n':
                        ChucNang6()
                    else:
                        print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
            elif choice==6.3:
                while True:
                    xacnhan=input("Xác nhận (Y/N): ")
                    if xacnhan=='Y' or xacnhan=='y':
                        print("Xác nhận thành công")
                        print()
                        print()
                        print()
                        kq=GiaiThichLyDo(thu_nhat,thu_hai)
                        lsdudoan.append([thu_nhat,thu_hai,kq])
                        return
                    elif xacnhan=='N' or xacnhan=='n':
                        ChucNang6()
                    else:
                        print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
            elif choice==6.4:
                while True:
                    xacnhan=input("Xác nhận (Y/N): ")
                    if xacnhan=='Y' or xacnhan=='y':
                        print("Xác nhận thành công")
                        print()
                        print()
                        print()
                        kq=DoUyTinDuDoan(thu_nhat,thu_hai)
                        lsdudoan.append([thu_nhat,thu_hai,kq])
                        return
                    elif xacnhan=='N' or xacnhan=='n':
                        ChucNang6()
                    else:
                        print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
            elif choice==0:
                return
            else:
                print("Nhập không có trong Menu vui lòng nhập lại")
    except ValueError:
        print("Phải nhập giá trị số nguyên ! Quay về trang chủ")
        return


#=======================================================================
def DoiGhiBanVuotTroi():
    content = _load_data()
    goals = [int(i['BT']) for i in content]
    tb = sum(goals) / len(goals)
    print("Các câu lạc bộ ghi bàn vượt trội:")
    for i in content:
        if int(i['BT']) - tb > 10:
            print(i['Câu lạc bộ'])


def DoiBiThungLuoiNhieu():
    content = _load_data()
    goals = [int(i['BB']) for i in content]
    tb = sum(goals) / len(goals)
    print("Các câu lạc bị thủng lưới nhiều:")
    for i in content:
        if int(i['BB']) - tb > 10:
            print(i['Câu lạc bộ'])


def HieuSuatKem():
    content = _load_data()
    print("Các câu lạc bộ có hiệu suất kém so với điểm số")
    for i in content:
        if int(i['HS'])<0:
            print(f"{i['Câu lạc bộ']}")


def NguyCoRotHang():
    content = _load_data()
    print("Các câu lạc bộ nguy cơ rớt hạng")
    for cnt, i in enumerate(content, 1):
        if int(i['HS'])<0 and int(i['T'])*2<int(i['B']) and cnt>=16:
            print(f"{i['Câu lạc bộ']}")


def ChucNang7():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("7.1 Đội ghi bàn vượt trội")
        print("7.2 Đội thủng lưới nhiều")
        print("7.3 Đội có hiệu suất kém so với điểm số")
        print("7.4 Cảnh báo nguy cơ xuống hạng")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==7.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    DoiGhiBanVuotTroi()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang7()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==7.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    DoiBiThungLuoiNhieu()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang7()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==7.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    HieuSuatKem()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang7()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==7.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    print()
                    print()
                    print()
                    NguyCoRotHang()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang7()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==0:
            return
        else:
            print("Nhập không có trong Menu vui lòng nhập lại")


#=======================================================================
def TaoFileTXT():
    file=input("Nhập tên file: ")
    content = _load_data()
    with open("Football_data/CreateFile/"+file,"w",newline="",encoding="UTF-8") as f:
        f.write("-"*122+"\n")
        f.write(f"| {'Hạng':<5} | {'Câu lạc bộ':<15} | {'Số trận':<8} | {'Thắng':<6} | {'Hòa':<4} | {'Thua':<5} | {'Bàn thắng':<10} | {'Bàn thua':<10} | {'Hiệu số':<8} | {'5 trận đấu gần nhất':<20} |"+"\n")
        f.write("-"*122+"\n")
        for i in content:
            f.write(f"| {i['Hạng']:<5} | {i['Câu lạc bộ']:<15} | {i['ST']:<8} | {i['T']:<6} | {i['H']:<4} | {i['B']:<5} | {i['BT']:<10} | {i['BB']:<10} | {i['HS']:<8} | {i['5_tran_gan_nhat']:<20} |"+"\n")
            f.write("-"*122+"\n")
    print("Đã tạo file TXT thành công !")


def TaoFileCSV():
    file=input("Nhập tên file: ")
    content = _load_data()
    with open("Football_data/CreateFile/"+file,"w",newline="",encoding="UTF-8") as f:
        fieldnames = list(content[0].keys())
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(content)
    print("Đã tạo file CSV thành công !")


def LuuLichSuFunction6(a):
    ds: dict[tuple[str, str], list[str]] = {}
    for doi1,doi2,noidung in a:
        key=(doi1,doi2)
        if key not in ds:
            ds[key]=[]
        ds[key].append(noidung)
    file=input("Nhập tên file: ")
    with open("Football_data/CreateFile/"+file,"w",newline="",encoding="UTF-8") as f:
        for key,value in ds.items():
            f.write(f"{key[0]} , {key[1]}"+"\n")
            for i in value:
                f.write(f"{i}"+"\n")
            f.write("\n")
    print("Đã tạo file dự đoán các đội bóng thành công !")


def FileKetQuaSoSanh(a):
    file=input("Nhập tên file: ")
    with open("Football_data/CreateFile/"+file,"w",newline="",encoding="UTF-8") as f:
        for i in a:
            f.write(i+"\n")
    print("Đã tạo file so sánh các đội bóng thành công !")


def ChucNang8():
    while True:
        print("===== Chọn chức năng chi tiết =====")
        print("8.1 Xuất bảng xếp hạng ra file TXT")
        print("8.2 Xuất thống kê đội bóng ra CSV")
        print("8.3 Lưu kết quả dự đoán")
        print("8.4 Lưu kết quả so sánh")
        print("0. Thoát")
        choice=float(input("Chọn: "))
        if choice==8.1:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    TaoFileTXT()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang8()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==8.2:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    TaoFileCSV()
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang8()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==8.3:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    LuuLichSuFunction6(lsdudoan)
                    return
                elif xacnhan=='N' or xacnhan=='n':
                    ChucNang8()
                else:
                    print("Nhập không phải Y hay N! Vui lòng xác nhận lại")
        elif choice==8.4:
            while True:
                xacnhan=input("Xác nhận (Y/N): ")
                if xacnhan=='Y' or xacnhan=='y':
                    print("Xác nhận thành công")
                    FileKetQuaSoSanh(lssosanh)
                    return
                elif xacnhan=='N' or xacnhan=='n':
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
        print("6.Dự đoán kết quả trận đấu")
        print("7.Thống kê & phát hiện bất thường")
        print("8.Báo cáo và xuất dữ liệu")
        print("0.Thoát")
        choice=int(input("Chọn chức năng: "))
        if choice==1:
            ChucNang1()
            return
        elif choice==2:
            ChucNang2()
            return
        elif choice==3:
            ChucNang3()
            return
        elif choice==4:
            ChucNang4()
            return
        elif choice==5:
            ChucNang5()
            return
        elif choice==6:
            ChucNang6()
            return
        elif choice==7:
            ChucNang7()
            return
        elif choice==8:
            ChucNang8()
            return
        elif choice==0:
            break
        else:
            print("Chọn không đúng giá trị chọn lại")


#============================================================================
while True:
    print("1.Bắt đầu chạy chương trình")
    choice=int(input("Chọn: "))
    if choice==1:
        main()
    else:
        print("Kết thúc chương trình")
        break
