import pandas as pd
from scipy.sparse import hstack
from sklearn.linear_model import Ridge
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

import sys
sys.path.append("..")
#from util import print_answer

def text_transform(text: pd.Series) -> pd.Series:
    return text.str.lower().replace("[^a-zA-Z0-9]", " ", regex=True)

def main():
    #task1
    train = pd.read_csv("salary-train.csv")
    print("Данные salary-train.csv")
    print(train.head())
    #task2
    vec = TfidfVectorizer(min_df=5)
    X_train_text = vec.fit_transform(text_transform(train["FullDescription"]))
    train["LocationNormalized"].fillna("nan", inplace=True)
    train["ContractTime"].fillna("nan", inplace=True)
    enc = DictVectorizer()
    X_train_cat = enc.fit_transform(train[["LocationNormalized", "ContractTime"]].to_dict("records"))
    X_train = hstack([X_train_text, X_train_cat])
    #task3
    y_train = train["SalaryNormalized"]
    model = Ridge(alpha=1)
    model.fit(X_train, y_train)
    #task4
    test = pd.read_csv("salary-test-mini.csv")
    X_test_text = vec.transform(text_transform(test["FullDescription"]))
    X_test_cat = enc.transform(test[["LocationNormalized", "ContractTime"]].to_dict("records"))
    X_test = hstack([X_test_text, X_test_cat])
    y_test = model.predict(X_test)
    print(f"{y_test[0]:.2f} {y_test[1]:.2f}")
    #print_answer(1, f"{y_test[0]:.2f} {y_test[1]:.2f}")





main()

