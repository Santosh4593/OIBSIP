# -*- coding: utf-8 -*-
"""Sales Prediction using python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YKiXPXuHn3SXcLln2kwJcEGtNCF4TsFk
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('/content/Advertising.csv')
df

"""#**EDA**"""

df.isnull().sum()

df.info()

df.describe()

plt.figure(figsize=[15,10])
sns.distplot(df['Sales'])
plt.title('Sales Distribution Plot')

plt.figure(figsize=(4,4))
sns.scatterplot(data=df,x=df['TV'],y=df['Sales'])
plt.show()

plt.figure(figsize=(4,4))
sns.scatterplot(data=df,x=df['Radio'],y=df['Sales'])
plt.show()

plt.figure(figsize=(4,4))
sns.scatterplot(data=df,x=df['Newspaper'],y=df['Sales'])
plt.show()

features = ['TV','Radio','Newspaper']
X = df[features]
y = df.Sales

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

"""# **Prediction** """

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.score(X_test,y_test)

model.predict(X_test)

from sklearn.tree import DecisionTreeRegressor
model2 = DecisionTreeRegressor()
model2.fit(X_train, y_train)

model2.score(X_test, y_test)

model2.predict(X_test)

from sklearn.ensemble import RandomForestRegressor
model3 = RandomForestRegressor(n_estimators=30)
model3.fit(X_train, y_train)

model3.score(X_test, y_test)

print("Linear Regression accuracy: ",model.score(X_test,y_test)*100)
print("Decision Tree accuracy: ",model2.score(X_test,y_test)*100)
print("Random Forest accuracy: ",model3.score(X_test,y_test)*100)

