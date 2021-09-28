# %%
# week 4 Thursday, numpy package
# functions; attributes; methods
# np array have to have the same data type, so we can do math 
import numpy as np
from numpy.core.defchararray import array
import random as random
import pandas as pd 

# %%
array1 = np.array([1,2,3])
array2 = np.array([(1,2,3),(4,5,6)])
array3 = np.ones((1,3))*6
array3.dtype
array3.dt
np.array()
# %%
a = np.random.randint(1,100,(6,12))
print(np.std(a))
print(np.mean(a[:,2]))
print(np.mean(a))
print(np.mean(a,axis=0)) #column mean 
print(np.mean(a,axis=1)) #row mean

# %%

# q1
x1 = np.array([i for i in range(1,11,1)  ])
x2 = 1.3

print(np.max(x1//x2))

# %%
# pandas series (1d) and data frame (2d)
# how to index: location- and lable-based
# mydataframe.iloc[rowselection, columnselection]
# mydataframe.loc[rowname,columnname]
# grab out individual columns
# mydata.frame.colname or mydataframe["colname"]
# methods: head, tail, sort (ascending or descending), describe, &
#          group by, min, median, max, sum, etc.

# %%
# Pandas Indexing Exercise 1
# start with the following dataframe of all 1's
data = np.ones((7, 3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# 1. Change the values for all of the vowel rows to 3
data_frame.loc[('a','e'),:] = 3
# 2. Multiply the first 4 rows by 7
data_frame.iloc[0:4,:] = data_frame.iloc[0:4,:] *4
# 3. Make the dataframe into a checkerboard  of 0's and 1's using loc
data_frame.loc['a',:] = [0,1,0]
data_frame.loc['b',:] = [1,0,1]
# 4. Same question as 3 but without using loc
for i in range(0,6):
    if i/2 
    data_frame.iloc[i,:] = [1,0,1]
# %%
