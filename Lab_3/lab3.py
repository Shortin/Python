import numpy as np
import matplotlib.pyplot as plt

data = np.matrix(np.loadtxt('ex1data1.txt', delimiter=','))
from matplotlib import rc
font = {'family': 'Verdana', 'weight': 'normal'}
rc('font', **font)
x = data[:, 0]
y = data[:, 1]
plt.plot(x, y, 'b.')
plt.title('Зависимость прибыльности от численности')
plt.xlabel('Численность')
plt.ylabel('Прибыльность')
plt.grid()
plt.show()


m = x.shape[0] # количество элементов в x (количество городов)
x_ones = np.c_[np.ones((m, 1)), x] # добавляем единичный столбец к x
theta = np.matrix('[1; 2]') # коэффициенты theta представляют собой вектор-столбец из 2 элементов
h_x = x_ones * theta # так можно вычислить значение гипотезы для всех городов сразу
# print(h_x)

def compute_cost(x, y, theta):
	h = theta[0, 0] + theta[1, 0] * x[1,0]
	i=1
	cost = 0
	while (i < m):
		cost1 = h * x[i, 0]-y[i, 0]
		cost1 = cost1**2
		cost1 = cost1 * (1/(2*m))
		print(cost1)
		cost += cost1
		i+=1
	return cost
print(compute_cost(x_ones, y, theta))