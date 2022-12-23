from scipy.io import loadmat
import numpy as np
from scipy.optimize import minimize
#from functions import add_zero_feature, sigmoid, decode_y,\
#    rand_initialize_weights, pack_params, unpack_params
from functions1 import add_zero_feature,pack_params,sigmoid,unpack_params,rand_initialize_weights
from functions1 import vectorized_result
from cost_function import cost_function
from sigmoid_gradient import sigmoid_gradient
from gradient_function import gradient_function
import pandas as pd
import json


if __name__ == '__main__':

    # Задание 1.
    # Загрузить обучающую выборку из файла training_set.mat в переменные X и y
    # Загрузить весовые коэффициенты из файла weights.mat в переменные Theta1 и Theta2
    # Использовать для этого функцию scipy.io.loadmat
    training_set = loadmat('training_set.mat')
    weights = loadmat('weights.mat')
    X = training_set['X']
    y = training_set['y'].ravel()
    Theta1 = weights['Theta1']
    Theta2 = weights['Theta2']
    m, n = X.shape
    # Задание 2.
    # Программно определить параметры нейронной сети
    # input_layer_size = ...  # количество входов сети (20*20=400)
    # hidden_layer_size = ... # нейронов в скрытом слое (25)
    # num_labels = ...        # число распознаваемых классов (10)
    # m = ...                 # количество примеров (5000)
    input_layer_size = n
    hidden_layer_size = 25
    num_labels = 10

    # добавление единичного столбца - нейрон смещения
    X = add_zero_feature(X)
    #TODO:
    # декодирование вектора Y
    #Y = decode_y(y)
    Y = np.zeros((m, num_labels))
    for i in range(m):
        Y[i, y[i] - 1] = 1

    # объединение матриц Theta в один большой массив
    nn_params = pack_params(Theta1, Theta2)

    # проверка функции стоимости для разных lambda
    lambda_coef = 0
    print('Функция стоимости для lambda {} = {}'.
          format(lambda_coef, cost_function(
            nn_params, input_layer_size, hidden_layer_size,
            num_labels, X, Y, lambda_coef)))

    lambda_coef = 1
    print('Функция стоимости для lambda {} = {}'.
          format(lambda_coef, cost_function(
            nn_params, input_layer_size, hidden_layer_size,
            num_labels, X, Y, lambda_coef)))

    # проверка производной sigmoid
    gradient = sigmoid_gradient(np.array([-1, -0.5, 0, 0.5, 1]))
    print('Производная функции sigmoid в точках -1, -0.5, 0, 0.5, 1:')
    print(gradient)

    # случайная инициализация параметров
    initial_Theta1 = rand_initialize_weights(input_layer_size, hidden_layer_size)
    initial_Theta2 = rand_initialize_weights(hidden_layer_size, num_labels)
    initial_nn_params = pack_params(initial_Theta1, initial_Theta2)

    # обучение нейронной сети
    res = minimize(cost_function, initial_nn_params, method='L-BFGS-B',
        jac=gradient_function, options={'maxiter': 100},
        args=(input_layer_size, hidden_layer_size, num_labels, X, Y, lambda_coef)).x

    # разбор вычисленных параметров на матрицы Theta1 и Theta2
    Theta1, Theta2 = unpack_params(
        res, input_layer_size, hidden_layer_size, num_labels)

    # выичисление отклика сети на примеры из обучающей выборки
    h1 = sigmoid(np.dot(X, Theta1.T))
    h2 = sigmoid(np.dot(add_zero_feature(h1), Theta2.T))
    y_pred = np.argmax(h2, axis=1) + 1

    print('Точность нейронной сети на обучающей выборке: {}'.format(
        np.mean(y_pred == y.ravel(), ) * 100))
