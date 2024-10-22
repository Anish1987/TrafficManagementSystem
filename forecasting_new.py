import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
import datetime  
#import tensorflow  
# from statsmodels.tsa.stattools import adfuller  
# from sklearn.preprocessing import MinMaxScaler  
# from tensorflow import keras  
# from keras import callbacks  
# from tensorflow.keras import Sequential  
# from tensorflow.keras.layers import Conv2D, Flatten, Dense, LSTM, Dropout, GRU, Bidirectional  
# from tensorflow.keras.optimizers import SGD  
import math  
# from sklearn.metrics import mean_squared_error  
  
import warnings  
warnings.filterwarnings("ignore")  

dataset = pd.read_csv("traffic.csv")  
dataset.head() 

dataset["DateTime"]= pd.to_datetime(dataset["DateTime"],infer_datetime_format=True,format='mixed')  
dataset.info()  

# dataframe to be used for EDA  
dataframe=dataset.copy()  
  
# Let's plot the Timeseries  
colors = [ "#FFD4DB","#BBE7FE","#D3B5E5","#dfe2b6"]  

dataframe["Year"]= dataframe['DateTime'].dt.year  
dataframe["Month"]= dataframe['DateTime'].dt.month  
dataframe.head() 

# Let's plot the Timeseries  
new_features = ["Month"] 

for i in new_features:  
    plt.figure(figsize=(15,6),facecolor="#627D78")  
    ax=sns.lineplot(x=dataframe[i],y="Vehicles",data=dataframe, hue="Junction", palette=colors )  
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  

plt.show()
