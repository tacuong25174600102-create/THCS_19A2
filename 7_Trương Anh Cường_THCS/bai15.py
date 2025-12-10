def bai_15_thuc_thi():
    while True:
        try:
            N = int(input("Nhập một số nguyên dương N: "))
            if N <= 0:
                print("Vui lòng nhập số nguyên dương.")
                continue
            break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
    if la_so_nguyen_to(N):
        print(f"-> {N} là SỐ NGUYÊN TỐ.")
    else:
        print(f"-> {N} KHÔNG phải là số nguyên tố.")
    print("-" * 30)
    print("Các số nguyên tố trong khoảng [100, 500]:")
    so_nguyen_to_tim_thay = []
    for n in range(100, 501):
        if la_so_nguyen_to(n):
            so_nguyen_to_tim_thay.append(n)
    print(so_nguyen_to_tim_thay)