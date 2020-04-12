import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
from sklearn.linear_model import LinearRegression

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


#multiple linear regresion

Z =df[["horsepower","curb-weight","engine-size","highway-mpg"]]
lm.fit(Z,df["price"])
Yhat1=lm.predict(Z)


#REsidual plot 
#sns.residplot(x=df["highway-mpg"], y=df["price"])        #regression plot 

# Distribution plot to compare the result real vs model results
ax1 = sns.distplot(df["price"], hist= False, color = "r" , label = "Actual Value")
sns.distplot(Yhat1, hist=False, color = "b" , label="fitted values")
plt.show()