import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\imports-85.data"

df = pd.read_csv(url, header = None,na_values="?")

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style",
"drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type",
"num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
"city-mpg","highway-mpg","price"]

df.columns=headers         #replace the columns header by the header variable

df_test = df[['drive-wheels',"body-style","price"]]  # sub matrix of df

print (df_test)

df_grp = df_test.groupby(["drive-wheels","body-style"],as_index=False).mean() # mean for every drive wheel and body style (grouped)
print (df_grp)

# pivot table
df_pivot = df_grp.pivot(index ="drive-wheels", columns="body-style")
print (df_pivot)
#print (df_pivot)

plt.pcolor(df_pivot,   cmap="RdBu")
plt.colorbar()
plt.xlabel("body-style")
plt.ylabel("drive-wheels")
plt.show()