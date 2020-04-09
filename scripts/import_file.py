import pandas as pd 

url = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\imports-85.data"

df = pd.read_csv(url, header = None)
print (df.head(2))    #Head filter data selecting the df.head(n) n first rows
print (df.tail(2))    #Head filter data selecting the df.tail(n) n final rows

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style",
"drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type",
"num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
"city-mpg","highway-mpg","price"]

df.columns=headers         #replace the columns header by the header variable

print (df.head(2))

path = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\automovile.csv"
df.to_csv(path)

print (df.dtypes)       # usefull to know which type of variable is stored by pandas importing
print (df.describe())     #  shows the statiticals information of the each column
print (df.describe(include = "all"))     #  shows the statiticals information of the each column including not numerical data

print (df.info())       #shows the first 30 rows values of dataset

