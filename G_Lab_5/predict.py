import numpy as np
from sigmoid import sigmoid
import scipy.io

def predict(Theta1, Theta2, X):
	# TODO: дополнить код в соответствии с методическими указаниями
	# 1. определить количество примеров (строк) в матрице X
	# m = ...
    m=X.shape[0]
    # 2. сгенерировать единичный вектор-столбец из m элементов
    # ones = ...
    ones=np.ones((m,1))
    # 3. получить a1, соединив единичный столбец и матрицу X
    # a1 = ...
    a1=np.c_[ones, X]
    # 4. вычислить значения на входах скрытого слоя сети, перемножив a1 на Theta1
    # z2 = ...
    z2=np.dot(a1,Theta1.T)
    # 5. вычислить значения на выходе скрытого слоя сети, применив сигмоиду к z2
    # a2 = ...
    a2=sigmoid(z2)
    a2=np.c_[ones, a2]
	# 6. вычислить значения на входах последнего слоя сети, перемножив a2 на Theta2
	# z3 = ...
    z3=np.dot(a2,Theta2.T)
	# 7. вычислить значения на выходах нейросети, применив сигмоиду к z3
	# h_x = ...
    h_x=sigmoid(z3)
    # 8. определить цифры, которые распознала сеть, используя функцию np.argmax
    # p = ...
    p=np.argmax(h_x,axis=1)
    return p+1


