tong_keo = int(input("Nhập tổng số kẹo: "))
so_hs = int(input("Nhập số học sinh: "))
moi_hs = tong_keo // so_hs
du = tong_keo % so_hs
print("Mỗi học sinh nhận:", moi_hs, "kẹo")
print("Số kẹo còn dư:", du, "kẹo")