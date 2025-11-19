n = int(input("Nhập n:"))
print("Các số nguyên tố nhỏ hơn", n, "là:")

for i in range(2, n):
    la_nguyen_to = True
    for j in range(2, i):
        if i % j == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        print(i, end=" ")
