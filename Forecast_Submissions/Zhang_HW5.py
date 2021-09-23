# Starter code for homework 5

# %%
# Import the modules we will use
import os
import numpy as np
from numpy.core.fromnumeric import shape
import pandas as pd
import matplotlib.pyplot as plt
import dataretrieval.nwis as nwis
import dataframe_image as dfi 


# %%
# download usgs streamflow data directly from NWIS and save as a dataframe

station_id = "09506000"
data = nwis.get_record(sites= station_id, service= 'dv', start= '1989-01-01',end= '2021-09-25', parameterCd='00060')

# %%
# ------------------------question 1----------------------------------------
# #What are the column names?
print(data.columns)

#What is its index?
print(data.index)

#What data types do each of the columns have?
data.dtypes

# %%
# ------------------------question 2----------------------------------------
#Provide a summary of the flow column including the min, mean, max, 
#standard deviation and quartiles.

# method 1
print(data["00060_Mean"].min())
print(data["00060_Mean"].mean())
print(data["00060_Mean"].median())
print(data["00060_Mean"].max())

print(data["00060_Mean"].std())

print(data["00060_Mean"].quantile([0,0.1,0.5,0.9]))

# method 2
data["00060_Mean"].describe()
# %%
# ------------------------question 3----------------------------------------
# the same information as in question 2 but on a monthly basis.
df = data.groupby(by=data.index.month).describe()
dfi.export(df,'./q3.png')
# %%
# ------------------------question 4----------------------------------------
#Provide a table with the 5 highest and 5 lowest flow values for the period of record. 
#Include the date, month and flow values in your summary.

# 5 highest flow values
print(data.sort_values(by= '00060_Mean').tail(5))

# 5 lowest flow values
data.sort_values(by= '00060_Mean').head(5)
# %%
# ------------------------question 5----------------------------------------
#Find the highest and lowest flow values for every month of the year
# (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.
 
# 12 mins and year
mins = pd.DataFrame({'Year': np.arange(1,13,1),
                        'Month': np.arange(1,13,1),
                        'Flow': np.zeros(12)})
mins = mins.set_index('Month')


mins['Flow'] = data.groupby(by=data.index.month).min()['00060_Mean']

for i in range(len(mins)):
        mins['Year'][i+1] = data.index[(data['00060_Mean'] == mins['Flow'][i+1]) \
                & (data.index.month == i+1)].year.values.astype('int')

# 12 maxs and year
maxs = pd.DataFrame({'Year': np.arange(1,13,1),
                        'Month': np.arange(1,13,1),
                        'Flow': np.zeros(12)})
maxs = maxs.set_index('Month')


maxs['Flow'] = data.groupby(by=data.index.month).max()['00060_Mean']

for i in range(len(maxs)):
        maxs['Year'][i+1] = data.index[(data['00060_Mean'] == maxs['Flow'][i+1]) \
                & (data.index.month == i+1)].year.values.astype('int')

# %%
# ------------------------question 6----------------------------------------
#Provide a list of historical dates with flows that are within 10% of your week 1 forecast value.
# If there are none than increase the %10 window until you have at least one other value 
# and report the date and the new window you used

week1_forecast = 200
upper_limit = week1_forecast*1.1
lower_limit = week1_forecast*0.9

array_q6 = data.index[(data['00060_Mean'] <= upper_limit) \
        & (data['00060_Mean'] >= lower_limit)].values
# %%
