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

df_anova= df[["make","price"]]  # Sub array
grouped_anova=df_anova.groupby(["make"])    #Gruped by make
anova_results_1=stats.f_oneway(grouped_anova.get_group("honda")["price"],grouped_anova.get_group("subaru")["price"])    #anova analysis Fvalue and pvalue
print (anova_results_1)


anova_results_2=stats.f_oneway(grouped_anova.get_group("honda")["price"],grouped_anova.get_group("jaguar")["price"])
print (anova_results_2)