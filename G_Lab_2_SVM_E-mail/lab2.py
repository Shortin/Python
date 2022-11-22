import numpy as np
import scipy.io
from sklearn import svm
from collections import OrderedDict

from process_email import process_email
from process_email import email_features
from process_email import get_dictionary


def main():
    with open('email.txt', 'r') as file:
        email=file.read().replace('\n','')
    word_indices=process_email(email)
    x = email_features(word_indices)
    print(len(x))
    
    print('train.mat')
    data = scipy.io.loadmat('train.mat')
    X = data['X']
    y = data['y'].flatten()
    print('Тренировка SVM-классификатора с линейным ядром...')
    clf = svm.SVC(C=0.1, kernel='linear', tol=1e-3)
    model = clf.fit(X, y)
    p = model.predict(X)
    print('Точность на обучающей выборке:',sum(p == y)/(sum(p == y)+sum(p != y))*100)
    #print('Точность на обучающей выборке:',np.mean(p==y)*100)

    print('test.mat')
   
    print('Тренировка SVM-классификатора с линейным ядром...')
    p = model.predict(X)

    #print('Точность на обучающей выборке:', sum(p == y) / (sum(p == y) + sum(p != y)) * 100)
    print('Точность на обучающей выборке:', np.mean(p == y) * 100)

    p = model.predict(x)

    # t = sorted(list(enumerate(model.coef_[0])), key=lambda e: e[1], reverse=True)
    # d = OrderedDict(t)
    # idx = list(d.keys())
    # weight = list(d.values())
    # dictionary = get_dictionary()
    # print('Топ-15 слов в письмах со спамом: ')
    # for i in range(15):
    #     print(' %-15s (%f)' % (dictionary[idx[i]], weight[i]))

main()

