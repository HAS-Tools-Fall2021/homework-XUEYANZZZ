# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()
np.size(flow_data)
np.ndim(flow_data)

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code:
# Start making your changes here. 

#NOTE: You will be working with the numpy array 'flow_data'
# Flow data has a row for every day and 4 columns:
# 1. Year
# 2. Month
# 3. Day of the month
# 4. Flow value in CFS


date_time = ["2021-09-12", "2021-09-13", "2021-09-14","2021-09-15","2021-09-16",\
        "2021-09-17","2021-09-18"]
date_time = pd.to_datetime(date_time)
data = flow_data[-7:,-1]

DF = pd.DataFrame()
DF['value'] = data
DF = DF.set_index(date_time)
plt.plot(DF)
plt.axhline(y=np.mean(data), color='r', linestyle='-')
plt.gcf().autofmt_xdate()
plt.xlabel("Date")
plt.ylabel("Observed flow (cfs)")
plt.savefig("obs.jpg",transparent=True,dpi=300)
plt.show()

# %%
