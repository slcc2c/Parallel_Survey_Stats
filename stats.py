import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

pd.set_option('display.max_colwidth', -1)

output = open('output.html', 'w')

df = pd.read_csv('results.csv')
output.write('<h1>The Data Frame</h1>')
output.write(df.to_html())

dfnums = df[df.columns[:4]]
dfwords = df[df.columns[4:]]
df
df_desc = dfnums.describe()

output.write('<h1>Descriptive Statistics</h1>')

output.write(df_desc.to_html())

axes = dfnums.boxplot(return_type='axes')
axes.set_ylim((0, 11))

output.write('<h1>Box Plot for each question</h1> <img src="img2.png" alt="Box Plot">')
plt.savefig('img2.png')

dfq2 = df.iloc[:, [0, 1]]
dfq2.columns = ['rating', 'satisfaction']
dfq3 = df.iloc[:, [0, 2]]
dfq3.columns = ['rating', 'satisfaction']
dfq4 = df.iloc[:, [0, 3]]
dfq4.columns = ['rating', 'satisfaction']

ax = dfq2.plot.scatter(x='satisfaction', y='rating', label='Q2', alpha=0.5)
ax = dfq3.plot.scatter(x='satisfaction', y='rating', color='orange', label='Q3', alpha=0.5, ax=ax)
dfq4.plot.scatter(x='satisfaction', y='rating', color='red', label='Q4', alpha=0.5, ax=ax)

output.write('<h1>Rating of material v. satisfaction w/ certain aspects of material</h1> <img src="img.png" alt="Scatter Plot">')

plt.savefig('img.png')

