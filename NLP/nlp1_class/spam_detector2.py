# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("../data/spambase.data").values

np.random.shuffle(data) # embaralhando meus dados

X = data[:, :48] # pega todas as linhas das primeiras 48 colunas
Y= data[:, -1] # pega todas as linhas da última coluna

Xtrain = X[:-100,]
Ytrain = Y[:-100,]
Xtest = X[-100:,]
Ytest = Y[-100:,]

classifier_NB = MultinomialNB()
classifier_NB.fit(Xtrain, Ytrain)
print("Classification rate for NB:", classifier_NB.score(Xtest, Ytest))


##### you can use ANY model! #####
from sklearn.ensemble import AdaBoostClassifier

model = AdaBoostClassifier()
model.fit(Xtrain, Ytrain)
print("Classification rate for AdaBoost:", model.score(Xtest, Ytest))

