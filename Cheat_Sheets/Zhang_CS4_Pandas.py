# %%
import pandas as pd 
import numpy as np
import csv 
from pandas.core.construction import array 
# Description: Pandas basics
# %% Question 1: What are they and how are they different from the other objects we have
# worded so far?

# Answer: Pandas dataframe includes different types of data, but one column only has one data type across
#         the whole rows, which is different from numpy array and list. Pandas dataframe have many attached 
#         methods! We can do calculation of Pandas dataframe. Also, a Pandas dataframe has row and column 
#         labels. 

# %% Question 2: How to make a pandas dataframe from scratch and by reading a csv

# Read from a csv
# data = pd.read_csv('data.csv')

# From scratch
data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
data = pd.DataFrame({'a': [1, 3, 2],
                    'b': [4, 6, 5],
                    'c': [7, 8, 9]})


# %% Question 3: How to slice pandas dataframes -- both using loc and iloc

# first add a row index
data['rowindex'] = ['row1', 'row2', 'row3']
data.set_index('rowindex', inplace=True)
# loc using row and column lables
data.loc['row2', 'a']

# iloc  using index
data.iloc[2,2]

# %% Question 4: What is the index of a pandas dataframe -- why is is different than other columns 
#                and how can you work with it?

# Answer: index is not a column. index is just a row label (string), and we use it to 
#         extract value. If the type of index is datetime, we can use many methods
#         related to datetime objects, such as data.index.yearand data.index.week. We also
#         can resample data based on our index!

data.dtypes # only shows types of three columns (a, b, c)
data.index 
data.index.values 

# %% Key methods associated with pandas dataframes

data.head(1)
data.tail(2)
data.describe()

# simple statistics: default calculate it on each column
data.mean()
data.max()
data.median()
data.std()
data.corr()

# Sort and filter data
data[data['a']>1]
data.sort_values('a')
data.groupby('a').mean()
data.groupby('b')['a'].sum()
data.apply(np.sum, axis=1) # axis=1: each row; axis=0: each column
data.drop(columns=['a'])

# Change data type
data['a'].astype('float')
# %% Key attributes associated with pandas dataframes
data.dtypes 
data.columns
data.index 
data.shape
data.size
data.iloc 
data.axes
data.T # Transpose 

# %% Summarize any additional functions 
# you have found helpful for working with dataframes

pd.concat([data, data], axis=1)
pd.melt(data)
pd.to_datetime(data['a'])
# pd.read_table('data.csv')