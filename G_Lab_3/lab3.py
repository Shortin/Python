import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

def compute_cost(x,y,theta):
    m = x.shape[0]
    cost=0
    for x,y in zip(x,y):
        cost+=np.power((x*(theta.T)-y),2)
    return cost/(2*m)

def gradient_descent(X,y,theta,alpha,iterations):
    temp_theta = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iterations)
    m = X.shape[0]
    J_theta = np.zeros((iterations,2))
    for i in range(iterations):
        h_x = (X * theta.T) - y
        for j in range(parameters):
            term = np.multiply(h_x, X[:, j])
            temp_theta[0, j] = theta[0, j] - ((alpha / m) * np.sum(term))
        theta = temp_theta
        cost[i] = compute_cost(X, y, theta)
        J_theta[i,0]=theta[0,0]
        J_theta[i, 1] = theta[0,1]
    return theta,cost
def S(x):
    sum=0
    n=len(x)
    for i in x:
        sum+=np.square((i-np.mean(x)))
    return np.sqrt(sum/(n-1))
def featureNormalize(X):
    mu = np.mean(X);
    sigma = np.std(X);
    X_norm = (X - mu)/sigma
    return X_norm, mu, sigma



#Задание 1
data = np.matrix(np.loadtxt('ex1data1.txt', delimiter=','))

#Задание 2
font = {'family': 'Verdana', 'weight': 'normal'}
rc('font', **font)
X = data[:, 0]
y = data[:, 1]
fig1, ax1 = plt.subplots(1,1)
ax1.plot(X, y, 'b.')
ax1.set_title ('Зависимость прибыльности от численности')
ax1.set_xlabel ('Численность')
ax1.set_ylabel ('Прибыльность')
ax1.grid()

#Задание 3
m=X.shape[0]
X_ones = np.c_[np.ones((m,1)),X]
theta = np.matrix('[1, 2]')
print('Ошибка:',compute_cost(X_ones,y,theta))

#Задание 4
theta = np.matrix('[0, 1]')
alpha=0.02
iterations=500
theta,cost=gradient_descent(X_ones,y,theta,alpha,iterations)
print('Расчитанный коэффициент',theta)
print('Новая ошибка',cost[-1])
fig, ax = plt.subplots()
ax.plot(np.arange(iterations), cost, 'b')
ax.set_title('Снижение ошибки при градиентном спуске')
ax.set_xlabel('Итерация')
ax.set_ylabel('Ошибка')
ax.grid()

#Задание 5


#Задание 6
fig2, ax2 = plt.subplots(1,1)
ax2.plot(X, y, 'b.')
ax2.set_title ('Зависимость прибыльности от численности')
ax2.set_xlabel ('Численность')
ax2.set_ylabel ('Прибыльность')
ax2.grid()
x=np.arange(min(X),max(X))
ax2.plot(x, theta[0,1]*x + theta[0,0], 'g--')


#Задание 7
data2 = np.matrix(np.loadtxt('ex1data2.txt', delimiter=','))
font = {'family': 'Verdana', 'weight': 'normal'}
rc('font', **font)
X = data2[:, :2]
Y = data2[:, 2]
m=len(Y)
X_norm,mean,sigma = featureNormalize(X)
X_ones = np.insert(X_norm,0,1,axis=1)
y=np.array(Y).reshape(-1,1)
theta=np.zeros([3,1])

#Задание 8
def computeCostMulti(X,y, theta):
    m = len(y)
    h = X*(theta)
    J=0
    for x,y in zip(X,y):
        J+=np.power((x*(theta)-y),2)
    return J/(2*m)

cost = computeCostMulti(X_ones,y,theta)
def gradientDescentMulti(X, y, theta, alpha, iter):
    J_history = []
    m = len(y)
    for i in range(iter):
        h = X.dot(theta)
        theta = theta - (alpha / m) * (X.T.dot(h - y))
        J_history.append(computeCostMulti(X, y, theta))
    return theta, J_history

iter = 400
iter_mass=[]
for i in range(iter):
    iter_mass.append(i)
alpha = 0.01
new_theta, J_history = gradientDescentMulti(X_ones, y, theta, alpha, iter)
J_mass=[]
for i in range(len(J_history)):
    J_mass.append(float(J_history[i]))
plt.plot(iter_mass,J_mass,'b-')
plt.ylabel('Cost J')
plt.xlabel('Number of Iterations')
plt.title('Minimizing Cost Using Gradient Descent')
plt.show()


#Задание 9
X = data2[:, :2]
X_ones = np.insert(X,0,1,axis=1)
Y = data2[:, 2]
theta=(np.linalg.pinv((np.transpose(X_ones))*X_ones))*np.transpose(X_ones)*Y
print(theta)
print(computeCostMulti(X_ones,y, theta))
#Задание 10
#Результат оценен


