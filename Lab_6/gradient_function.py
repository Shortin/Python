import numpy as np
from functions1 import sigmoid, add_zero_feature, pack_params,unpack_params
from sigmoid_gradient import sigmoid_gradient


def gradient_function(nn_params, input_layer_size, hidden_layer_size,
                      num_labels, X, Y, lambda_coef):

    Theta1, Theta2 = unpack_params(
        nn_params, input_layer_size, hidden_layer_size, num_labels)

    # Задание 5.
    # Реализовать функцию gradient_function

    # количество примеров
    # m = ...
    m = X.shape[0]
    # вычисление отклика нейронной сети
    # A_1 = ...
    # Z_2 = ...
    # A_2 = ...
    # A_2 = ...
    # Z_3 = ...
    # A_3 = ...
    ones = np.ones((m, 1))
    A_1 = X
    Z_2 = np.dot(A_1, Theta1.T)
    A_2 = sigmoid(Z_2)
    A_2 = np.c_[ones, A_2]
    Z_3 = np.dot(A_2, Theta2.T)
    A_3 = sigmoid(Z_3)

    # вычисление ошибок по нейронам
    # DELTA_3 = ...
    #DELTA_3=A_3-Y
    # DELTA_2 = ...
    #DELTA_2=DELTA_3.T.dot(A_2)

    # вычисление частных производных
    # Theta1_grad = ...
    # Theta2_grad = ...

    # добавление регуляризатора
    # Theta1_grad[:, 1:] += ...
    # Theta2_grad[:, 1:] += ...
    d_3 = A_3 - Y
    D_2 = d_3.T.dot(A_2)

    Z_2 = np.hstack((np.ones((m, 1)), Z_2))
    d_2 = d_3.dot(Theta2) * sigmoid_gradient(Z_2)
    d_2 = d_2[:, 1:]
    D_1 = d_2.T.dot(X)

    Theta_1_grad = 1.0 * D_1 / m
    Theta_1_grad[:, 1:] = Theta_1_grad[:, 1:] + 1.0 * lambda_coef / m * Theta1[:, 1:]

    Theta_2_grad = 1.0 * D_2 / m
    Theta_2_grad[:, 1:] = Theta_2_grad[:, 1:] + 1.0 * lambda_coef / m * Theta2[:, 1:]

    return pack_params(Theta_1_grad, Theta_2_grad)
