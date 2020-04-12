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
r"""
SCALE=StandardScaler()
SCALE.fit(x_data[["horsepower","highway-mpg"]])
x_scale=SCALE.transform(x_data[["horsepower","highway-mpg"]])
pr =PolynomialFeatures(degree=2,include_bias=False)
"""
Input = [("scale",StandardScaler()),("polinomial",PolynomialFeatures(degree=2)),("mode",LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(df[["horsepower","curb-weight","engine-size","highway-mpg"]],df["price"])
yhat = pipe.predict(df[["horsepower","curb-weight","engine-size","highway-mpg"]])

ax1 = sns.distplot(df["price"], hist= False, color = "r" , label = "Actual Value")
sns.distplot(yhat, hist=False, color = "b" , label="fitted values")
plt.show()