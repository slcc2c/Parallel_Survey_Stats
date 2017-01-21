import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
import statsmodels.formula.api as sm

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

q1counts = dfnums['Q1'].value_counts()
q1countsort = q1counts.sort_index()


q2counts = dfnums['Q2'].value_counts()
q2countsort = q2counts.sort_index()

q3counts = dfnums['Q3'].value_counts()
q3countsort = q3counts.sort_index()


d = {'Q1': q1counts, 'Q2':q2counts, 'Q3':q3counts}
dfcounts = pd.DataFrame(d)

output.write('<h1>Frequency of Responses</h1>'+dfcounts.to_html())


output.write('<h1>Box Plot for each question</h1> <img src="img2.png" alt="Box Plot">')
plt.savefig('img2.png')

plt.close()

dfq2 = df.iloc[:, [0, 1]]
dfq2.columns = ['rating', 'satisfaction']
dfq3 = df.iloc[:, [0, 2]]
dfq3.columns = ['rating', 'satisfaction']
dfq4 = df.iloc[:, [0, 3]]
dfq4.columns = ['rating', 'satisfaction']

ax = dfq2.plot.scatter(x='satisfaction', y='rating', label='Q1', alpha=0.5)
ax = dfq3.plot.scatter(x='satisfaction', y='rating', color='orange', label='Q2', alpha=0.5, ax=ax)
dfq4.plot.scatter(x='satisfaction', y='rating', color='red', label='Q3', alpha=0.5, ax=ax)

output.write(
    '<h1>Overall Rating v. satisfaction w/ specific aspects of material</h1> <img src="img.png" alt="Scatter Plot">')

plt.savefig('img.png')

plt.close()


result = sm.ols(formula='Q1 ~ Q2 + Q3 + Q4', data=df).fit()

output.write('<h1>Linear Regression:Q1=Q2+Q3+Q4</h1><div><pre>'+str(result.summary())+'</pre></div>')

result = sm.ols(formula='Q1 ~ Q2 + Q4', data=df).fit()

output.write('<h1>Linear Regression:Q1=Q2+Q4</h1><div><pre>'+str(result.summary())+'</pre></div>')

result = sm.ols(formula='Q4 ~ Q3', data=df).fit()

output.write('<h1>Linear Regression:Q4=Q3</h1><div><pre>'+str(result.summary())+'</pre></div>')

Q1pol = []
Q2pol = []
Q3pol = []
Q1sub = []
Q2sub = []
Q3sub = []

for row in dfwords.itertuples():

    if row[1] != '.':
        sentiment = TextBlob(row[1])
        Q1sub.append(sentiment.sentiment.polarity)
        Q1pol.append(sentiment.sentiment.polarity)
    if row[2] != '.':
        sentiment = TextBlob(row[2])

        Q2sub.append(sentiment.sentiment.subjectivity)
        Q2pol.append(sentiment.sentiment.polarity)
    if row[3] != '.':
        sentiment = TextBlob(row[3])

        Q3sub.append(sentiment.sentiment.subjectivity)
        Q3pol.append(sentiment.sentiment.polarity)

output.write('<h1>Sentiment Analysis</h1>')
d = {'Q4 polarity': pd.Series(Q1pol), 'Q4 subjectivity': pd.Series(Q1sub), 'Q5 polarity': pd.Series(Q2pol),
     'Q5 subjectivity': pd.Series(Q2sub), 'Q6 polarity': pd.Series(Q3pol), 'Q6 subjectivity': pd.Series(Q3sub)}
df_sent = pd.DataFrame(d)

output.write(df_sent.to_html())
output.write('<h1>Sentiment Analysis Stats</h1>')
dfpol = df_sent.iloc[:, [0, 2, 4]]
dfpol_stat = dfpol.describe()
output.write(dfpol_stat.to_html())

output.write('<h1>Sentiment Analysis Graphs</h1> <img src="img3.png" alt="Sentiment">')
axes = dfpol.boxplot(return_type='axes')
axes.set_ylim((-1, 1))
axes.set_ylabel('Polarity')
axes.set_xlabel('')
plt.savefig('img3.png')
