def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Vô số nghiệm (a=0, b=0)"
        else:
            return "Vô nghiệm (a=0, b!=0)"
    else:
        x = -b / a
        return f"Nghiệm x = {x}"