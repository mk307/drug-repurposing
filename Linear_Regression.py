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

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(train_scaled, y_train)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

mse = mean_squared_error(y_train, model.predict(train_scaled))
mae = mean_absolute_error(y_train, model.predict(train_scaled))

from math import sqrt

print("mse = ",mse," & mae = ",mae," & rmse = ", sqrt(mse))

test_mse = mean_squared_error(y_test, model.predict(test_scaled))
test_mae = mean_absolute_error(y_test, model.predict(test_scaled))
print("mse = ",test_mse," & mae = ",test_mae," & rmse = ", sqrt(test_mse))
