luong_co_ban = float(input("Nhập mức lương cơ bản (VND): "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))
luong_moi_ngay = luong_co_ban / 22
luong_thang = luong_moi_ngay * so_ngay_cong
if so_ngay_cong > 22:
    luong_thang *= 1.10   # thưởng 10%
elif so_ngay_cong < 22:
    luong_thang *= 0.95   # phạt 5%
print(f"Lương thực nhận: {luong_thang:.0f} VND")