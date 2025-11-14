gia = float(input("Nhập giá sản phẩm (VND): "))
so_luong = int(input("Nhập số lượng mua: "))
tong = gia * so_luong
vat = tong * 0.10
phai_tra = tong + vat
print(f"Tổng tiền phải trả (đã gồm VAT): {phai_tra:.2f} VND")