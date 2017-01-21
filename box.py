import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
import statsmodels.formula.api as sm

pd.set_option('display.max_colwidth', -1)

output = open('output2.html', 'w')


df = pd.read_csv('box.csv')
output.write('<h1>The Data</h1>')
output.write(df.to_html())

axes = df.boxplot(return_type='axes')
axes.set_ylim((0, 20))

output.write('<h1>Box Plot for each question</h1> <img src="img4.png" alt="Box Plot">')
plt.savefig('img4.png')