import matplotlib.pyplot as plt
import numpy as np
from sklearn import  linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import csv
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LogisticRegression
#import matplotlib.pyplot as plt

data = pd.read_csv('dataset_features_test.csv')

x =data[['Positive Emotion','Negative Emotion','Anxiety','Anger','Death','Feel','Health','Articles',
         'Auxiliary Verbs','Conjunctions','Adverbs','Personal Pronouns',
        'function','Assent','Certainty']].values
#print(x)
print('x shape:',x.shape)
#
target = pd.read_csv('Data.csv')
y =target['disease'].values
#print(y)
print('y shape:', y.shape)
#
#
#convert to array to fit the model
x=np.asarray(x)
y=np.asarray(y)

# print(x)
# print(y)

n = x.shape[0]
n_train = int(np.round(n * 0.9))
n_valid = n - n_train

idx = np.random.permutation(n)
x = x[idx,:]
y = y[idx]

# Split the data into training/testing sets
disease_X_train = x[:n_train,:] #
disease_X_test = x[n_train:, :]  #

print('train X:',disease_X_train.shape)
print('test X:',disease_X_test.shape)

# Split the targets into training/testing sets
disease_y_train = y[:n_train]
disease_y_test = y[n_train:]

print('train target:',disease_y_train.shape)
print('test target:',disease_y_test.shape)

logreg = LogisticRegression()
logreg.fit(disease_X_train, disease_y_train)
disease_y_pred1 = logreg.predict(disease_X_test)


data = pd.read_csv('dataset_features.csv')

x_test =data[['Positive Emotion','Negative Emotion','Anxiety','Anger','Death','Feel','Health','Articles',
         'Auxiliary Verbs','Conjunctions','Adverbs','Personal Pronouns',
         'function','Assent','Certainty']].values


#pred = regr.predict(x_test)
pred = logreg.predict(x_test)

infname='Merged_all_fornow.csv'
tweets = pd.read_csv(infname)
# print(tweets)
tweets['disease'] = pred
tweets.to_csv('prediction_tweets.csv',  index=False, columns = ['disease','text'])



