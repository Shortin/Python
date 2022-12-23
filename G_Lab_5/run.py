import scipy.io
from displayData import displayData
import numpy as np
from predict import predict
import matplotlib.pyplot as plt

def main():
    test_set=scipy.io.loadmat('test_set.mat')
    weights = scipy.io.loadmat('weights.mat')
    X = test_set['X']
    y = test_set['y'].flatten()
    Theta1=weights['Theta1']
    Theta2=weights['Theta2']
    m=X.shape[0]
    rand_index=np.random.permutation(m)
    X_rand=np.zeros((0,400))
    for i in range(100):
        X_rand=np.vstack([X_rand,X[rand_index[i]]])
    displayData(X_rand[:100])
    pred = predict(Theta1, Theta2, X)
    y=y.ravel()
    result=[]
    for i in range(len(y)):
        if np.double(y[i])==np.double(pred[i]):
            result.append(True)
        else:
            result.append(False)
    print(np.mean(result)*100)

    rp = np.random.permutation(m)
    plt.figure()
    for i in range(5):
        X2 = X[rp[i], :]
        X2 = np.matrix(X[rp[i]])
        pred = predict(Theta1, Theta2, X2.getA())
        pred = np.squeeze(pred)
        pred_str = 'Neural Network Prediction: %d (digit %d)' % (pred, y[rp[i]])
        displayData(X2, pred_str)
        plt.close()

    pred = predict(Theta1, Theta2, X)
    mistake=np.where(pred!=y.ravel())[0]
    X_mistake=np.zeros((0,400))
    for i in range(100):
        X_mistake=np.vstack([X_mistake,X[mistake[i]]])
    displayData(X_mistake[:100])

main()