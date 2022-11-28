from recommendations import critics
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy

def P(c1,c2):
    sum=0
    for item in critics[c1]:
        if item in critics[c2]:
            sum+=(critics[c1][item]-critics[c2][item])**2
    return 1/(1+math.sqrt(sum))
print(P('Кот Матроскин','Дядя Фёдор'))
film1='Ну, погоди!'
film2='Зима в Простоквашино'
film1_matr=[]
film2_matr=[]
film_matr=[]
for item in critics:
    if film1 in critics[item]:
        film1_matr.append(critics[item][film1])
    else:
        continue
    if film2 in critics[item]:
        film2_matr.append(critics[item][film2])
        film_matr.append(item)
    else:
        film1_matr.pop()
        continue
plt.plot(film1_matr,film2_matr, 'b.')
for f1,f2,f in zip(film1_matr,film2_matr,film_matr):
    plt.text(f1,f2,f,horizontalalignment='left',
        verticalalignment='top')
plt.xlabel(f'Оценка за фильм {film1}')
plt.ylabel(f'Оценка за фильм {film2}')
plt.grid()
plt.xlim(0,5)
plt.ylim(0,5)
plt.show()
plt.close()


def sim_distance(prefs, person1, person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0:
        return 0
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)

print(sim_distance(critics,'Кот Матроскин','Пёс Шарик'))



def sim_pearson(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item] = 1
    n = len(si)
    if n == 0: return 0
    sum1 = sum([prefs[person1][it] for it in si])
    sum2 = sum([prefs[person2][it] for it in si])
    sum1Sq = sum([pow(prefs[person1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[person2][it], 2) for it in si])
    pSum = sum([prefs[person1][it] * prefs[person2][it] for it in si])
    num = pSum - (sum1 * sum2 / n)
    den = math.sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0
    r = num / den
    return r

def P1(X,Y,N):
    a1=sum(X*Y)-(sum(X)*sum(Y))/N
    a2=math.sqrt()
print(sim_pearson(critics,'Кот Матроскин','Пёс Шарик'))

author1='Кот Матроскин'
author2='Галчонок'
film_rating1=[]
film_rating2=[]
nameFilm = []
for item in critics[author1]:
    if item in critics[author2]:
        film_rating1.append(critics[author1][item])
        film_rating2.append(critics[author2][item])
        nameFilm.append(item)

plt.xlabel(f'{author1}')
plt.ylabel(f'{author2}')
plt.grid()
plt.xlim(2.3,4.1)
plt.ylim(2.8,5.2)
print(min(film_rating1))
slope, intercept, r, *__ = scipy.stats.linregress(film_rating1, film_rating2)
plt.plot(film_rating1,film_rating2, 'b.')
fx = np.array([min(film_rating1), max(film_rating1)])
plt.plot(fx,(intercept + slope * fx), 'r')
for f1,f2,f in zip(film_rating1,film_rating2,nameFilm):
    plt.text(f1,f2,f,horizontalalignment='left',
        verticalalignment='top')

plt.show()

def top_matches(prefs,person):
    similarity = sim_pearson
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:len(critics)]

print(top_matches(critics,'Кот Матроскин'))