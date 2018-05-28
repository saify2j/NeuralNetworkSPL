import numpy as np
data=np.genfromtxt("wine.txt",delimiter=",",dtype=float)

np.set_printoptions(precision=3,suppress=True,threshold=np.nan,linewidth=150)


data2=data[:,1:]

#print(data)
class1=class2=class3=0


for i in range (data.shape[0]):
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

print ("Number Of features Per Class :" +str(data2.shape[1]))


x=data2
#print(x)


for i in range(x.shape[0]):
    for j in range (x.shape[1]):
        while(x[i][j]>=1):

            x[i][j]/=10

#print(x)


y=data[:,[0]]



print(y)

y2=np.zeros((y.shape[0],3))

#print(y2)

for i in range (y.shape[0]):
    if (y[i]==1):
        y2[i][1-1]=1
    if (y[i]==2):
        y2[i][2-1]=1
    if (y[i]==3):
        y2[i][3-1]=1

#print("------")
#print(y2)
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigDer(x):
    return x*(1-x)


learnRate=0.5

inputLayer=x.shape[1] #column number gula e hobe input layer

hiddenLayer=17 #iccha moto neya jai ektu beshi nile accuracy bare , but ekta shomoy jeye ar defer kore na

outputLayer=3


#erpor layer gular weight set kora lagbe

weightOfHiddenlayer=np.random.uniform(size=(inputLayer,hiddenLayer))

#print(weightOfInputlayer)

biasOfHiddenlayer=np.random.uniform(size=(1,hiddenLayer))

weightOfOutputlayer=np.random.uniform(size=(hiddenLayer,outputLayer))

biasOfOutputlayer=np.random.uniform(size=(1,outputLayer))

#forward propagation

for i in range(10000):
    hiddenLayerTempInput = np.dot(x, weightOfHiddenlayer)

    # print(hiddenLayerTempInput)

    hiddenLayerInput = hiddenLayerTempInput + biasOfHiddenlayer

    hiddenLayerActivationInputs = sigmoid(hiddenLayerInput)

    outputLayerTempInput = np.dot(hiddenLayerActivationInputs, weightOfOutputlayer)

    outputLayerInput = outputLayerTempInput + biasOfOutputlayer

    output = sigmoid(outputLayerInput)

    # backpropagation

    error = y2 - output

    slopeOfOutputLayer = sigDer(output)

    slopeOfHiddenLayer = sigDer(hiddenLayerActivationInputs)

    effectOnOutput = error * slopeOfOutputLayer

    errorAtHiddenLayer = effectOnOutput.dot(weightOfOutputlayer.T)

    effectOnHiddenLayer = errorAtHiddenLayer * slopeOfHiddenLayer

    weightOfOutputlayer += hiddenLayerActivationInputs.T.dot(effectOnOutput) * learnRate
    if(i==10000-1):
        break


    # bias update

    biasOfOutputlayer += np.sum(effectOnOutput, axis=0, keepdims=True) * learnRate
    weightOfHiddenlayer += x.T.dot(effectOnHiddenLayer) * learnRate
    biasOfHiddenlayer += np.sum(effectOnHiddenLayer, axis=0, keepdims=True) * learnRate


print(output)


# #TESTING DATA
#
#
#
# testData=np.genfromtxt("w2.txt",delimiter=",",dtype=float)
# x2=testData[:,1:]
# print(x2)
# for i in range(x2.shape[0]):
#     for j in range (x2.shape[1]):
#         while(x2[i][j]>=1):
#
#             x2[i][j]/=10
#
#
#
# hiddenLayerTempInput = np.dot(x2, weightOfHiddenlayer)
# hiddenLayerInput = hiddenLayerTempInput + biasOfHiddenlayer
#
# hiddenLayerActivationInputs = sigmoid(hiddenLayerInput)
#
# outputLayerTempInput = np.dot(hiddenLayerActivationInputs, weightOfOutputlayer)
#
# outputLayerInput = outputLayerTempInput + biasOfOutputlayer
#
# output = sigmoid(outputLayerInput)
#
#
# print(output)
