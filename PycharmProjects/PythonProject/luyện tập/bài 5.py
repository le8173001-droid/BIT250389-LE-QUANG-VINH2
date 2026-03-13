M=int(input("nhập hệ số"))
N=int(input("nhập hệ số"))
hang=int(input("nhập hàng"))
cot=int(input("nhập côt"))
import numpy as np
matrix = np.random.randint(0,11,size=(M,N))
print(matrix)
print("cot",cot,matrix[cot-1])
print("hang",hang,matrix[hang-1])
print("gía trị lớn nhất",np.max(matrix))



