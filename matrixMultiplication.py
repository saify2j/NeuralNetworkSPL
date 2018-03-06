def multiplymatrix(a, b):
    res= []
    for i in range(0, len(a)):
        res.append([])

    for i in range(0, len(a)):
        for j in range(0, len(b[0])):
            res[i].append(j)
            res[i][j]= 0

    for i in range(0, len(a)):
        for j in range(0, len(b[0])):
            for k in range(0, len(b)):
                res[i][j]+= a[i][k]*b[k][j]

    return res


a= [[2,3],
    [4,5],
    [6,7]]
b=[[1,3,5],
   [4,5,6]]
print(multiplymatrix(a,b))


#
#
# a= [[1, 2],
#     [2, 2],
#     [3,3]]
# b= [[1, 2],
#     [2, 2]]
# res=[]
# #print(len(a), len(a[0]))
#
# for i in range(0,len(a)):
#     res.append([])
#
# for i in range(0, len(a)):
#     for j in range(0, len(b[0])):
#         res[i].append(j)
#         res[i][j]= 0
#
# for i in range(0,len(a)):
#     for j in range(0,len(b[0])):
#
#         for k in range(0,len(b)):
#             res[i][j]+=a[i][k]*b[k][j]
#
# print(res)

