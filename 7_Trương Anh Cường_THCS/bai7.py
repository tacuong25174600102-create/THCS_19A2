def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
def tong_so_hoan_hao(a, b):
    tong = 0
    so_hoan_hao_tim_thay = []
    for n in range(a, b + 1):
        if la_so_hoan_hao(n):
            tong += n
            so_hoan_hao_tim_thay.append(n)
    return tong