def kiem_tra_so_armstrong(n):
    if not isinstance(n, int) or n < 0:
        return False
    chuoi_n = str(n)
    so_chu_so = len(chuoi_n)
    if so_chu_so != 3:
        return False
    tong_luy_thua = 0
    temp_n = n
    while temp_n > 0:
        chu_so = temp_n % 10
        tong_luy_thua += so_chu_so # Trong Python có thể dùng  3 hoặc ** so_chu_so
        temp_n //= 10
    return tong_luy_thua == n