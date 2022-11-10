import scipy.io as sio
import numpy as np
import svm


def main():

    #task1
    data = sio.loadmat('dataset1.mat')
    X = data['X']
    y = data['y'].astype(np.float64)
    svm.visualize_boundary_linear(X, y, None, title='Исходные данные')
    
    #task2
    C=1
    model = svm.svm_train(X, y, C, svm.linear_kernel, 0.001, 20)
    svm.visualize_boundary_linear(X, y, model, title='Разделяющаю граница при С=1')
    
    #task3
    C=100
    model = svm.svm_train(X, y, C, svm.linear_kernel, 0.001, 20)
    svm.visualize_boundary_linear(X, y, model, title='Разделяющаю граница при С=100')
    
    #task4
    svm.contour(1)
    svm.contour(3)
    
    #task5
    data = sio.loadmat('dataset2.mat')
    X = data['X']
    y = data['y'].astype(np.float64)
    svm.visualize_data(X, y).show()
    
    #task6
    C = 1
    sigma = 0.1
    gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
    gaussian.__name__ = svm.gaussian_kernel.__name__
    model= svm.svm_train(X, y, C, gaussian)
    svm.visualize_boundary(X, y, model)
    
    #task7
    data = sio.loadmat('dataset3.mat')
    X = data['X']
    y = data['y'].astype(np.float64)
    Xval = data['Xval']
    yval = data['yval'].astype(np.float64)
    svm.visualize_data(X, y).show()
    svm.visualize_data(Xval, yval).show()
    
    #task8
    C=1
    sigma=0.5
    gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
    gaussian.__name__ = svm.gaussian_kernel.__name__
    model= svm.svm_train(X, y, C, gaussian)
    svm.visualize_boundary(X, y, model)
    
    #task9
    best_C = 0
    best_sigma = 0
    best_error = len(yval)
    best_model = None
    for C in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
        for sigma in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
            gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
            gaussian.__name__ = svm.gaussian_kernel.__name__
            model = svm.svm_train(X, y, C, gaussian)
            ypred = svm.svm_predict(model, Xval)
            error = np.mean(ypred != yval.ravel())
            if error < best_error:
                best_error = error
                best_C = C
                best_sigma = sigma
                best_model = model

    print(f"Best C = {best_C}, best sigma = {best_sigma}, best Error = {best_error}")
    svm.visualize_boundary(X, y, best_model)
    svm.visualize_boundary(Xval, yval, best_model)

main()