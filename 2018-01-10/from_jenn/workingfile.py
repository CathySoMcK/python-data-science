import pandas as pd

df = pd.read_csv('KCLT.csv')
df.info()
# change oject to date/time
df['date'] = pd.to_datetime(df.date)

#filtering in Pandas
df[df.actual_mean_temp < 81].info

df.describe  # you can describe the entire dataset, or just one column
df.actual_mean_temp.describe()  # just one column

df[df.actual_mean_temp < 19].date  #which date was it less than 19 degrees

df[(df.actual_mean_temp < 20) | (df.actual_mean_temp > 86)].date  #more than one filter

df[(df.actual_mean_temp < 20) | (df.actual_mean_temp > 86)][['date','actual_mean_temp']] # show more than one column

#filter by date
df[df.date > '2015-06-01'].date

#tell me the year, month day for record "0"
df.date[0].year
df.date[0].month
df.date[0].day


pandas.read_excel
