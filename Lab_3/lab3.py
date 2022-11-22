import numpy as np
import matplotlib.pyplot as plt

#Задание 1
data = np.matrix(np.loadtxt('ex1data1.txt', delimiter=','))

#Задание 2
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

#Задание 3
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
print(compute_cost(x, y, theta))
#ПРОВЕРЬ ЭТУ ХУЙНЮ ЛЕХА, КАЖЕТЯ ЧТО-ТО НЕ ТАК


#Задание 4
def gradient_descent(X, y, alpha, iterations):
 # определение m – количество городов в матрице X (матрица X должна содержать единичный столбец). 
# Используйте свойство X.shape для определения m и n.
#  # определение n – количество столбцов в матрице X (в нашей задаче n = 2)
#  # создать вектор-столбец theta и инициализировать его первый элемент нулем, а остальные элементы 
# единицами. Количество элементов в theta равно n.
#  # создать вектор-столбец J_theta, размер которого равен количеству итераций, заполненный нулями
#  # запустить цикл по итерациям: for i in range(iterations):
#  # вычислить значение ошибки J_theta[i] для текущих значений theta
#  # модифицировать коэффициенты theta по формуле 4 (не забудьте про использование временной 
# переменной temp_theta)
