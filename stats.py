import pandas as pd
import numpy as np

df = pd.read_csv('results.csv')
dfnums = df[df.columns[:4]]
dfwords = df[df.columns[4:]]

print dfnums.describe()