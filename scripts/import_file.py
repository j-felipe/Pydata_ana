import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

url = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\imports-85.data"

df = pd.read_csv(url, header = None,na_values="?")
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
print (df["symboling"]) #accesing just a "symboling Column"
print (df["body-style"])
#df["symboling"]=df["symboling"]+1  #adding 1 to all "symboling series"
#print (df["symboling"])

#print (df.head(20))    #Head filter data selecting the df.head(n) n first rows


df.dropna(subset = ["price"], axis = 0, inplace =True) #eliminates de entire Row (axis=0 entire row axis =1 entire column) if no value is found
#inplace = True means that the modification is done on the data set directly
print (df.head(20))
path = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\automovile_droping_price.csv"
df.to_csv(path)

mean = df["normalized-losses"].mean()

df["normalized-losses"]=df["normalized-losses"].replace(np.nan, mean) #replace the empty (NaN) data by mean 

path = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\automovile_replacing_normalized-loses.csv"
df.to_csv(path)

##### Transform milles per gallon to litres per 100 km
df["city-mpg"]= 235/df["city-mpg"]   # change entire column
df.rename(columns={"city-mpg":"city-L/100"}, inplace=True)  #rename de header
path = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\automovile_mpg-l100.csv"
df.to_csv(path)

print (df["price"].dtypes)        #identify the data type of the data
df["price"]=df["price"].astype("int")   #convert the data to Int type
print (df.head(20))

#simple feature normalization

df["length"]=df["length"]/df["length"].max()
path = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\automovile_lengthN.csv"
df.to_csv(path)

#Min-Max normalization

r"""
df["length"]=(df["length"]-df["length"].min())/(df["length"].max()-df["length"].min())
path = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\automovile_lengthMM.csv"
df.to_csv(path)
"""
#Z-score normalization
r"""
df["length"]=(df["length"]-df["length"].mean())/(df["length"].std())
path = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\automovile_lengthMM.csv"
df.to_csv(path)
"""
####Bining or grouped 
bins= np.linspace(min(df["price"]),max(df["price"]),4)      # generates 4 equal space gruop of data 
print (bins)
groupe_name= ["low", "mid", "high"]
df["price-binned"]=pd.cut(df["price"],bins,labels=groupe_name,include_lowest=True) #creates a new column with binnet price data
path = r"C:\Users\HP\Desktop\2020_04_10_Datas_Analysis_python\data\automovile_pricebinned.csv"
df.to_csv(path)
print (df["price-binned"])
df["price"].plot.hist(bins=3)
plt.show()

#### convert object in numerical (Categorical into variables) 
Dummy = pd.get_dummies(df["fuel-type"])     #creates new array assingning 1 or 0 if the catagorical variable is found ()
print  (Dummy)
