import numpy as np
from functions1 import sigmoid, add_zero_feature
#from functions1 import sigmoid, add_zero_feature, unpack_params


def cost_function(nn_params, input_layer_size, hidden_layer_size, num_labels,
                  X, Y, lambda_coef):

    # распаковка параметров
    #Theta1, Theta2 = unpack_params(
    #    nn_params, input_layer_size, hidden_layer_size, num_labels)
    Theta1 = np.reshape(nn_params[0:(hidden_layer_size * (input_layer_size + 1)), ],
                         (hidden_layer_size, input_layer_size + 1))
    Theta2 = np.reshape(nn_params[(hidden_layer_size * (input_layer_size + 1)):, ],
                         (num_labels, hidden_layer_size + 1))
    # Задание 3.
    # Реализовать функцию ошибки нейронной сети

    # количество примеров
    # m = ...
    m = X.shape[0]
    # вычисление отклика нейронной сети
    ones = np.ones((m, 1))
    # A_1 = ...
    A_1=X
    # Z_2 = ...
    Z_2=np.dot(A_1,Theta1.T)
    # A_2 = ...
    A_2=sigmoid(Z_2)
    # A_2 = ...
    A_2=np.c_[ones, A_2]
    # Z_3 = ...
    Z_3=np.dot(A_2,Theta2.T)
    # A_3 = ...
    A_3=sigmoid(Z_3)
    # H = ...
    H=Z_3

    # вычисление ошибки
    # J = ...
    '''Y = np.zeros((m, num_labels))
    for i in range(m):
        Y[i, y[i] - 1] = 1'''
    J = 0.0
    for i in range(m):
        J += np.log(A_3[i, ]).dot(-Y[i, ].T) - np.log(1 - A_3[i, ]).dot(1 - Y[i, ].T)
    J /= m

    # вычисление регуляризатора
    # reg_J = ...
    Theta_1_square = np.square(Theta1[:, 1:])
    Theta_2_square = np.square(Theta2[:, 1:])
    reg_J = 1.0 * lambda_coef / (2 * m) * (np.sum(Theta_1_square) + np.sum(Theta_2_square))
    J += reg_J

    return J
