import pandas as pd
from math import sqrt
import numpy as np

data = pd.read_excel("/Users/meikeepauline/Desktop/IP/DataPD.xlsx")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(data)
      
print(data.head())
print(data.info())
print(data.describe())

