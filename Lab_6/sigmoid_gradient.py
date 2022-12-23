import numpy as np
from functions1 import sigmoid


def sigmoid_gradient(z):

    # Задание 4.
    # Реализовать функцию вычисления производной от сигмоида в точке (точках) z
    # derivative = ...
    derivative=sigmoid(z) * (1 - sigmoid(z))
    return derivative
