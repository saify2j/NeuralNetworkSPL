import numpy as np
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))


x=np.array([ [0,0],
             [0,1],
             [1,0],

           ])
y=np.array([[0,0,0]]).T


np.random.seed(1)



syn0 = 2*np.random.random((2,1)) - 1


for iter in range(10000):
    l0=x

    l1=nonlin(np.dot(l0,syn0))

    l1_error = y - l1

    l1_delta= l1_error * nonlin (l1,True)

    syn0+=np.dot(l0.T,l1_delta)


    print ("Output after training")
    print (l1)