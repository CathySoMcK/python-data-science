import pandas as pd
df = pd.read_csv('supplies.csv')

#add a new column called total = units * unitsprice
df['Total'] = df['Units'] * df['Unit Price']

#show the mean, sum for each rep per region
regions = df.groupby(['Region','Rep'])['Total'].agg(['mean', 'sum', 'count'])

#which are the largest?
largestthree = df.groupby(['Region','Rep'])['Total'].agg(['mean', 'sum', 'count']).nlargest(3, 'mean')

regions = df.groupby(['Region'])['Total'].agg(['sum'])
reps = df.groupby(['Region'])['Rep'].unique()


#convert series into dataframe
rps = reps.to_frame()
reps = rps.reset_index()
regions = regions.reset_index()
merged = pd.merge(reps, regions, on='Region', how='inner').set_index('Region')


merged['count'] = merged.apply(lambda row: len(row['Rep']), axis=1)
merged['normalized'] = merged['sum'] / merged['count']
