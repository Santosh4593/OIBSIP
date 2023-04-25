# -*- coding: utf-8 -*-
"""Car Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q7UfDKKH_fKM5YzqTkf0Vmjx_A-OfgxK
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv('/content/CarPrice.csv')
df

df.isnull().sum()

df.info()

"""# **Visualization**"""

plt.figure(figsize=[15,10])
sns.distplot(df['price'])
plt.title('Car Price Distribution Plot')

df.price = df.price.astype(int)
y= df['price']
data=["symboling", "wheelbase", "carlength", 
             "carwidth", "carheight", "curbweight", 
             "enginesize", "boreratio", "stroke", 
             "compressionratio", "horsepower", "peakrpm", 
             "citympg", "highwaympg"]

x = df[data]

y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,train_size=0.8)

"""# **Prediction**"""

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(x_train,y_train)

model.score(x_test,y_test)

model.predict(x_test)

