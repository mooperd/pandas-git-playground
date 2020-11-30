import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)
dataframe = pd.read_csv("git-log-2020.csv")
dataframe['date'] = pd.to_datetime(dataframe['date'])

# function that runs per group
def my_function(row):
    print("hello")
    return row['email'].value_counts().sort_values(ascending = False).head(3)

top_three = dataframe.groupby(pd.Grouper(key='date', freq='1M')).apply(my_function)

print(top_three)

fig, ax = plt.subplots(figsize=(6, 10))
top_three.unstack().plot(kind='bar', ax=ax, stacked=True)
plt.show()