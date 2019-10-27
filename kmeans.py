import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from sklearn.preprocessing import scale
seaborn.set()
# %matplotlib inline

data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv")
del data["Channel"]
del data["Region"]
data.head()


data_array = data.values
kmeans = KMeans(n_clusters=5, init='k-means++', n_init=10, random_state=1234)
data["clusters"] = kmeans.fit_predict(data_array)
data.groupby("clusters").aggregate("mean").plot.bar(figsize=(10,7.5))
plt.title("Gastos por cluster")