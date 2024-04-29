import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv

cols = ['S(dr,do)', 'S(dr,dn)', 'S(do,dn)', 'Score(dr,di)']
data = pd.read_csv('Data.csv', nrows = 42, usecols = cols)

from sklearn.model_selection import train_test_split

X = data.drop(["Score(dr,di)"], axis=1)
y = data["Score(dr,di)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

X_train.shape
X_test.shape

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

train_scaled = scaler.fit_transform(X_train)
test_scaled = scaler.fit_transform(X_test)

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

tree_model = DecisionTreeRegressor()
rf_model = RandomForestRegressor()

tree_model.fit(train_scaled, y_train)
rf_model.fit(train_scaled, y_train)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

tree_mse = mean_squared_error(y_train, tree_model.predict(train_scaled))
tree_mae = mean_absolute_error(y_train, tree_model.predict(train_scaled))
rf_mse = mean_squared_error(y_train, rf_model.predict(train_scaled))
rf_mae = mean_absolute_error(y_train, rf_model.predict(train_scaled))

from math import sqrt

print("Decision Tree training mse = ",tree_mse," & mae = ",tree_mae," & rmse = ", sqrt(tree_mse))
print("Random Forest training mse = ",rf_mse," & mae = ",rf_mae," & rmse = ", sqrt(rf_mse))

tree_test_mse = mean_squared_error(y_test, tree_model.predict(test_scaled))
tree_test_mae = mean_absolute_error(y_test, tree_model.predict(test_scaled))
rf_test_mse = mean_squared_error(y_test, rf_model.predict(test_scaled))
rf_test_mae = mean_absolute_error(y_test, rf_model.predict(test_scaled))

print("Decision Tree test mse = ",tree_test_mse," & mae = ",tree_test_mae," & rmse = ", sqrt(tree_test_mse))
print("Random Forest test mse = ",rf_test_mse," & mae = ",rf_test_mae," & rmse = ", sqrt(rf_test_mse))
