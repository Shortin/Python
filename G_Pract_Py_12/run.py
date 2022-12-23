import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

#task1
df=pd.read_csv('close_prices.csv')
print(df.head())
X=df.loc[:,"AXP":]

#task2
pca=PCA(n_components=10)
pca.fit(X)
sum_var = 0
for i, v in enumerate(pca.explained_variance_ratio_):
    sum_var += v
    if sum_var >= 0.9:
        break
print("\nКомпоненты, необходимые для объяснения 90% дисперсии: ",i+1)
print()
#task3
X0 = pd.DataFrame(pca.transform(X))[0]
print(X0.head())

#task4
df2 =pd.read_csv("djia_index.csv")
print(df.head())
corr=np.corrcoef(X0,df2["^DJI"])
print("Корреляция Пирсона между первой компонентой и индексом Доу-Джонса: ",end='')
print(f"{corr[1, 0]:.2f}")

#task5
print("Компания имеющая наибольший вес в первой компоненте: ", end='')
print(X.columns[np.argmax(pca.components_[0])])
