import numpy as np
X = np.array([[1, 0],
              [1,1 ],
              [0, 1],
              ])
#prints row of array

#print(X.shape[0])

#prints collum of array

#print(X.shape[1])

Y = np.array([[1],
              [0],
              [1]])


def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigDer(x):
    return x*(1-x)

learnRate=0.5

inputLayer=X.shape[1] #column number gula e hobe input layer

hiddenLayer=5 #iccha moto neya jai ektu beshi nile accuracy bare , but ekta shomoy jeye ar defer kore na

outputLayer=1

#erpor layer gular weight set kora lagbe

weightOfHiddenlayer=np.random.uniform(size=(inputLayer,hiddenLayer))

#print(weightOfInputlayer)

biasOfHiddenlayer=np.random.uniform(size=(1,hiddenLayer))

weightOfOutputlayer=np.random.uniform(size=(hiddenLayer,outputLayer))

biasOfOutputlayer=np.random.uniform(size=(1,outputLayer))

#forward propagation

for i in range(10000):
    hiddenLayerTempInput = np.dot(X, weightOfHiddenlayer)

    # print(hiddenLayerTempInput)

    hiddenLayerInput = hiddenLayerTempInput + biasOfHiddenlayer

    hiddenLayerActivationInputs = sigmoid(hiddenLayerInput)

    outputLayerTempInput = np.dot(hiddenLayerActivationInputs, weightOfOutputlayer)

    outputLayerInput = outputLayerTempInput + biasOfOutputlayer

    output = sigmoid(outputLayerInput)

    # backpropagation

    error = Y - output

    slopeOfOutputLayer = sigDer(output)

    slopeOfHiddenLayer = sigDer(hiddenLayerActivationInputs)

    effectOnOutput = error * slopeOfOutputLayer

    errorAtHiddenLayer = effectOnOutput.dot(weightOfOutputlayer.T)

    effectOnHiddenLayer = errorAtHiddenLayer * slopeOfHiddenLayer

    weightOfOutputlayer += hiddenLayerActivationInputs.T.dot(effectOnOutput) * learnRate



    # bias update

    biasOfOutputlayer += np.sum(effectOnOutput, axis=0, keepdims=True) * learnRate
    weightOfHiddenlayer += X.T.dot(effectOnHiddenLayer) * learnRate
    biasOfHiddenlayer += np.sum(effectOnHiddenLayer, axis=0, keepdims=True) * learnRate


print(output)
