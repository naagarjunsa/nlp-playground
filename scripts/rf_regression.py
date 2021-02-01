import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV

df = pd.read_csv('../data/car-data.csv')

df['Current_Year'] = 2020
df['Age'] = df['Current_Year'] - df['Year']
df = df.drop(labels = ['Current_Year', 'Year', 'Car_Name'], axis = 1)
df = pd.get_dummies(df, drop_first = True)

X = df.iloc[:,1:]
y = df.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size = 0.2)

rf_random = RandomForestRegressor()

#HyperParameters for RandomForestRegressor
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(5, 30, num=6)]
min_samples_split = [2,5,10,15,100]
min_samples_leaf = [1,2,5,10]

random_grid = {'n_estimators' : n_estimators,
               'max_features' : max_features,
               'max_depth' : max_depth,
               'min_samples_split' : min_samples_split,
               'min_samples_leaf' : min_samples_leaf}

rf = RandomForestRegressor()
rf_random = RandomizedSearchCV(estimator = rf,
                               param_distributions = random_grid,
                               scoring = 'neg_mean_squared_error',
                               n_iter = 10, cv = 5,
                               verbose = 2, random_state = 42,
                               n_jobs = 1)
rf_random.fit(X_train, y_train)


with open('../models/car_price_prediction.pkl', 'wb') as f:
    pickle.dump(rf_random, f)
