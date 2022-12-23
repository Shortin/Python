import numpy as np
from scipy.special import expit

def add_zero_feature(array):
    return np.insert(array, 0, 1, axis=1)

def pack_params(Theta1,Theta2):
    return np.concatenate((Theta1.flat, Theta2.flat))

def sigmoid(z):
    g_z=expit(z)
    return g_z

def unpack_params(nn_params, input_layer_size, hidden_layer_size, num_labels):
    Theta_1 = np.reshape(nn_params[0:(hidden_layer_size * (input_layer_size + 1)), ],
                         (hidden_layer_size, input_layer_size + 1))
    Theta_2 = np.reshape(nn_params[(hidden_layer_size * (input_layer_size + 1)):, ],
                         (num_labels, hidden_layer_size + 1))
    return Theta_1,Theta_2

def rand_initialize_weights(l_in, l_out):
    epsilon_init = 0.12
    W = np.random.rand(l_out, 1 + l_in) * 2 * epsilon_init - epsilon_init
    return W

def vectorized_result(j):
 e = np.zeros((10, 1))
 e[j] = 1.0
 return e
