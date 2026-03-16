can_nang=float(input("nhập cân nặng:kg"))
chieu_cao=float(input("nhập chiều cao:m"))

def tinh_BMI():
    return(round(can_nang/chieu_cao ** 2,2))
print(tinh_BMI())


