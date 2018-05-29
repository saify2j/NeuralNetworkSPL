import numpy as np

#Input array
X=np.array([[1,1],
            [0,0,],
            [0,1],
            [1,0]])

#Output
y=np.array([[0],[0],[1],[1]])

#Sigmoid Function


def sigmoid (x):

    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function


def derivatives_sigmoid(x):

    return x * (1 - x)

#Variable initialization

epoch=10000
learningRate=0.5

inputlayer_neurons = X.shape[1]

hiddenlayer_neurons = 5

output_neurons = 1

weigh_hidden=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))

bh=np.random.uniform(size=(1,hiddenlayer_neurons))

weight_out = np.random.uniform(size=(hiddenlayer_neurons,output_neurons))


bout=np.random.uniform(size=(1,output_neurons))



for i in range(epoch):

#Forward Propogation

    hidden_layer_input1=np.dot(X,weigh_hidden)

    hidden_layer_input=hidden_layer_input1 + bh

    hiddenlayer_activations = sigmoid(hidden_layer_input)

    output_layer_input1=np.dot(hiddenlayer_activations,weight_out)

    output_layer_input= output_layer_input1+ bout

    output = sigmoid(output_layer_input)


#Backpropagation

    Error = y-output

    slope_output_layer = derivatives_sigmoid(output)

    slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)

    d_output = Error * slope_output_layer

    Error_at_hidden_layer = d_output.dot(weight_out.T)

    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer

    weight_out += hiddenlayer_activations.T.dot(d_output) * learningRate
#this update part is a bit unclear to me 
    bout += np.sum(d_output, axis=0,keepdims=True) * learningRate

    weigh_hidden += X.T.dot(d_hiddenlayer) * learningRate

    bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) * learningRate

print (output)
