
import numpy as np
#
# a=np.array([[2,3],[4,6]])
# b=np.array([[2,3],[4,6]])
#
# c=np.array([[1,2,3,-3],
#             [4,5,6,-2],
#             [7,8,9,-1]])
#
# #print(a.dot(b)) matrix multiplication
#
# #print(c[:3,1:3]) this helps to get a part of the matrix
#
# d=np.random.random((2,2))
# print(d)




a= [[1, 2],
    [2, 2],
    [3,3]]
b= [[1, 2],
    [2, 2]]
res=[]
#print(len(a), len(a[0]))

for i in range(0,len(a)):
    res.append([])

for i in range(0, len(a)):
    for j in range(0, len(b[0])):
        res[i].append(j)
        res[i][j]= 0

for i in range(0,len(a)):
    for j in range(0,len(b[0])):

        for k in range(0,len(b)):
            res[i][j]+=a[i][k]*b[k][j]

print(res)
