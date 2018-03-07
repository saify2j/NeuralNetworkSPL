def transpose(a):
    res=[]
    for i in range (len(a[0])):
        temp=[]
        for j in range(len(a)):
            x=a[j][i]
            temp.append(x)
        res.append(temp)
    return res



print(transpose([[1,2],
   [3,4],
   [5,6]]
))