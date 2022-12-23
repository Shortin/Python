import scipy.io
import numpy as np
from functions1 import add_zero_feature,pack_params
from sigmoid_gradient import sigmoid_gradient
from cost_function import  cost_function
training_set = scipy.io.loadmat('training_set.mat')
weights = scipy.io.loadmat('weights.mat')
X = training_set['X']
y = training_set['y'].flatten()
Theta1 = weights['Theta1']
Theta2 = weights['Theta2']
m, n = X.shape

X=add_zero_feature(X)
nn_params=pack_params(Theta1,Theta2)
sg=sigmoid_gradient([-1, -0.5, 0, 0.5, 1])

input_layer_size = n
hidden_layer_size = 25
num_labels = 10

cf=cost_function(nn_params,input_layer_size,hidden_layer_size,num_labels,X,y,lambda_coef=0)
1