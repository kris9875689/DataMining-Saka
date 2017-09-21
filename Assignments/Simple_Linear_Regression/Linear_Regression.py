
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 07:58:22 2017

@author: KrishnaSaka
"""
# This program gives us the result of Linear Regression between the Interest Rates and Median Home Price.
# where Median Home price is the dependent value and Interest Rates is Independent one.
# we plot the graph between those by taking the independent value Interest rates on x axis and 
# dependent variable Median Home Price on y-axis where predict the data based on trained data.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Dataset
dataset = pd.read_csv('Data.csv') 
a = dataset.iloc[:, :-1].values
b = dataset.iloc[:, 1].values

#splitting the Dataset into the Training set and Test set

from sklearn.cross_validation import train_test_split
a_train, a_test, b_train, b_test = train_test_split(a, b, test_size = 1/3, random_state = 0)

#Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(a_train, b_train)

#Predicting the test Results
b_pred = regressor.predict(a_test)

#visualising the Training set results
plt.scatter(a_train, b_train, color = 'red' )
plt.plot(a_train, regressor.predict(a_train), color = 'blue')
plt.title('interest_rates vs Medain_home_price (Training set)')
plt.xlabel('interest rates')
plt.ylabel('median home price')
plt.show()


#visualising the Test set results
plt.scatter(a_test, b_test, color = 'red' )
plt.plot(a_train, regressor.predict(a_train), color = 'blue')
plt.title('interest_rates vs Medain_home_price (Test set)')
plt.xlabel('interest rates')
plt.ylabel('median home price')
plt.show()
