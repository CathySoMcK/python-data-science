import pandas as import pd
import morestats as m

df = pd.read_csv('baseball.csv')

#find average height, weight, age for all players using morestats

avg_height  = m.mean(df.Height)
avg_weight  = m.mean(df.Weight)
avg_age  = m.mean(df.Age)

#group by team name and show mean height, weight, ages
teams = df.groupby(['Team']).mean()

#find aggregate stats for Arizona
arizona = teams.loc[ARZ]

#which team has the greatest average Height
greatest = teams.idxmax()['Height']
