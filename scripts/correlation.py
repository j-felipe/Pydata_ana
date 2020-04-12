import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

url = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\imports-85.data"

df = pd.read_csv(url, header = None,na_values="?")

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style",
"drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type",
"num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
"city-mpg","highway-mpg","price"]

df.columns=headers         #replace the columns header by the header variable
r"""
sns.regplot(x="engine-size", y="price", data=df)        #regression plot 
plt.ylim(0,)
plt.show()


sns.regplot(x="highway-mpg", y="price", data=df)        #regression plot 
plt.ylim(0,)
plt.show()

sns.regplot(x="peak-rpm", y="price", data=df)        #regression plot 
plt.ylim(0,)
plt.show()
"""
df.dropna(subset = ["horsepower"], axis = 0, inplace =True)     #eliminates de empty or Nan values
df.dropna(subset = ["price"], axis = 0, inplace =True)     #eliminates de empty or Nan values
sns.regplot(x="horsepower", y="price", data=df)        #regression plot 
plt.ylim(0,)

person_coef ,p_value = stats.pearsonr(df["horsepower"],df["price"])
print(person_coef)
print (p_value)
plt.show()