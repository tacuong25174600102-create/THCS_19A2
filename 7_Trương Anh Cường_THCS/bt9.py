kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))
if kwh <= 100:
    tien = kwh * 1678
elif kwh <= 200:
    tien = 100 * 1678 + (kwh - 100) * 1734
else:   # từ 201 trở lên, dùng bậc 3 cho phần còn lại
    tien = 100 * 1678 + 100 * 1734 + (kwh - 200) * 2014
print(f"Tổng tiền điện: {tien:.0f} VND")
