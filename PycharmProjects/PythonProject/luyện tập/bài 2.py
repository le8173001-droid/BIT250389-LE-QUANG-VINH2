a=float(input("nhập hệ số"))
b=float(input("nhập hệ số"))
def luy_thua():
    return(a**b),(b**a)
print (luy_thua())
def căn_bậc_hai():
    return(a**1/2),(b**1/2)
print(căn_bậc_hai())
def chia_lay_phan_nguyen():
    return(a//b)
print(chia_lay_phan_nguyen())
def chia_lay_phan_du():
    return(a%b)
print(chia_lay_phan_du())
def làm_tròn_số():
    return(round(a),round(b))
print(làm_tròn_số())