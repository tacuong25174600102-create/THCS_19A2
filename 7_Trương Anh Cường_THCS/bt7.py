username = input("Nhập tên đăng nhập: ")
password = input("Nhập mật khẩu: ")

if username == "admin" and password != "password123":
    print("Truy cập được cấp.")
else:
    print("Từ chối truy cập.")