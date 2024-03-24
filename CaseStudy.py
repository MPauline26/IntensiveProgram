import pandas as pd
from math import sqrt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("/Users/meikeepauline/Desktop/IP/DataPD.xlsx")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
      
print(data.head())
print(data.info())
print(data.describe())

""" for col in data:
    sns.displot(data[col])
    sns.boxplot(data[col])

plt.show() """

correlation = data.corr()

print(correlation)