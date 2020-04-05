import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

""" ========== Simple Linear Regression ========== """

base = pd.read_csv('mt_cars.csv')
base = base.drop(['Unnamed: 0'],axis=1)


X = base.iloc[:,2].values
y = base.iloc[:,0].values

correlation = np.corrcoef(X,y)

X = X.reshape(-1,1)

model = LinearRegression()
model.fit(X,y)
model.intercept_
model.coef_
model.score(X,y) # R²

# Adjusted R² 
model_adj = sm.ols (formula = 'mpg ~ disp', data = base) # adjusted model
model_trn = model_adj.fit() # trained model
model_trn.summary()
plt.scatter(X,y) #dispersion graph
plt.plot(X,model.predict(X),color = 'red')

# For disp = 200, mpg = ?

model.predict([[200]])

""" ========== Multiple Linear Regression ========== """

X1 = base.iloc[:,1:4].values
y1 = base.iloc[:,0].values

model1 = LinearRegression()
model1.fit(X1,y1)

# Adjusted R² 
model1_adj = sm.ols (formula = 'mpg ~ cyl + disp + hp', data = base) # adjusted model
model1_trn = model1_adj.fit() # trained model
model1_trn.summary()

# For cyl = 4, disp = 200, hp = 100, mpg = ?
condition = np.array([4,200,100]).reshape(1,-1)
model1.predict(condition)

