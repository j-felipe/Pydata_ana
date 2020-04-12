import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error                
     
url = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\imports-85.data"

df = pd.read_csv(url, header = None,na_values="?")

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style",
"drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type",
"num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
"city-mpg","highway-mpg","price"]

df.columns=headers         #replace the columns header by the header variable

df.dropna(subset = ["price"], axis = 0, inplace =True)
df.dropna(subset = ["horsepower"], axis = 0, inplace =True)
df.dropna(subset = ["curb-weight"], axis = 0, inplace =True)
df.dropna(subset = ["engine-size"], axis = 0, inplace =True)
df.dropna(subset = ["highway-mpg"], axis = 0, inplace =True)



lm=LinearRegression()
x =df[["highway-mpg"]]
y=df["price"]
lm.fit(x,y)         # REaliza la regression y obtiene los parametros de la regresion lineal
Yhat=lm.predict(x)      # Se puede usar para untriducir valores y ver resutados segun el modelo de regresion obtenido
lin_pre=(np.array(30.0).reshape(-1,1))
print (lm.score(x,y))       # Value R para evaluar cuan bueno es nuetro modeloç
new_value = np.arange(1,101,1).reshape(-1,1)
lin_pre1=lm.predict(new_value)



#multiple linear regresion

Z =df[["horsepower","curb-weight","engine-size","highway-mpg"]]
lm.fit(Z,df["price"])
Yhat1=lm.predict(Z)
#lin_pre1=(np.array(30.0).reshape(-1,1)) # create a valida value to predict function
new_value = np.arange(1,101,1).reshape(-1,1)



 # polinomial Regression
Input = [("scale",StandardScaler()),("polinomial",PolynomialFeatures(degree=2)),("mode",LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(df[["horsepower","curb-weight","engine-size","highway-mpg"]],df["price"])
Yhat2 = pipe.predict(df[["horsepower","curb-weight","engine-size","highway-mpg"]])
lin_pre2=(np.array(30.0).reshape(-1,1))


ax1 = sns.distplot(df["price"], hist= False, color = "gray" , label = "Actual Value")
sns.distplot(Yhat, hist=False, color = "b" , label="fitted values linear")
sns.distplot(Yhat1, hist=False, color = "y" , label="fitted values multilinear")
sns.distplot(Yhat2, hist=False, color = "g" , label="fitted values poly 2")

#sns.distplot(lin_pre, hist=False, color = "r" , label="predict 1")
sns.distplot(lin_pre1, hist=False, color = "r" , label="predict 2")
#sns.distplot(lin_pre2, hist=False, color = "r" , label="predict 3")

mean_sq_e_1= mean_squared_error(df["price"],Yhat)
mean_sq_e_2= mean_squared_error(df["price"],Yhat1)
mean_sq_e_3= mean_squared_error(df["price"],Yhat2)


print (mean_sq_e_1)
print (mean_sq_e_2)
print (mean_sq_e_3)


plt.show()