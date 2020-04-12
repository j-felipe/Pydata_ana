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
print (df.describe())     #  shows the statiticals information of the each column

drive_wheel_counts = df["drive-wheels"].value_counts()      # Count by variable into this array
#df.rename(columns={"drive-wheels":"value_counts"}, inplace = True)
print (df.head(2))
print (df.info())
print (drive_wheel_counts)
#print (drive_wheel_counts.describe())
drive_wheel_counts.index.name="drive-wheels"
print (drive_wheel_counts)
#drive_wheel_counts.rename(columns={"drive-wheels":"value_counts"}, inplace = True)  #doesn't works looks like beacouse is not a panda frame
print (drive_wheel_counts)

boxplt=sns.boxplot(x = "drive-wheels", y = "price", data=df)   # Box plot 
plt.show()

y = df["price"]
x = df["engine-size"]
scatter = plt.scatter(x,y)
plt.title("Scatter plot of Engine size Vs price")               #scatter plot
plt.xlabel("Size")
plt.ylabel("Price")
plt.show()


