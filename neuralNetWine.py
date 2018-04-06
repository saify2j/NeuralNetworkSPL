import numpy as np
data=np.genfromtxt("wine.txt",delimiter=",",dtype=float)

np.set_printoptions(precision=3,suppress=True,threshold=np.nan,linewidth=150)


data2=data[:,1:]

#print(data)
class1=class2=class3=0
x=data.shape[0]
for i in range (x):
    if data[i][0]==1:
        class1+=1
    elif data[i][0]==2:
        class2+= 1
    else:
        class3+= 1

print("Total Number Of data:"+str(i+1))

print("--------")
print("Number Of Class 1 Wine:"+str(class1))
print("Number Of Class 2 Wine:"+str(class2))
print("Number Of Class 3 Wine:"+str(class3))




#print(data2)


