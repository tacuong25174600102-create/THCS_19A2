tien_gui = float(input("Nhập số tiền gửi ban đầu (VND): "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): "))
r = lai_suat_nam / 100
lai_1_thang = tien_gui * r * (1/12)
lai_2_quy = tien_gui * r * 0.5
lai_3_nam = tien_gui * r * 3 
print(f"Lãi sau 1 tháng: {lai_1_thang:.2f} VND")
print(f"Lãi sau 2 quý (6 tháng): {lai_2_quy:.2f} VND")
print(f"Lãi sau 3 năm: {lai_3_nam:.2f} VND")