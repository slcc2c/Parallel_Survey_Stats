import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib



df = pd.read_csv('results.csv')
dfnums = df[df.columns[:4]]
dfwords = df[df.columns[4:]]
df
print dfnums.describe()

dfq2 = df.iloc[:, [0,1]]
dfq2.columns = ['rating', 'satisfaction']
dfq3 = df.iloc[:, [0,2]]
dfq3.columns = ['rating', 'satisfaction']
dfq4 = df.iloc[:, [0,3]]
dfq4.columns = ['rating', 'satisfaction']

ax = dfq2.plot.scatter(x='satisfaction', y='rating', label='Q2', alpha=0.5)
ax = dfq3.plot.scatter(x='satisfaction', y='rating', color='orange', label='Q3', alpha=0.5, ax=ax)
dfq4.plot.scatter(x='satisfaction', y='rating', color='red', label='Q4', alpha=0.5, ax=ax)
plt.show()

