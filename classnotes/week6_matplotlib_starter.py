# Starter code for week 7 illustrating how to build an AR model 
# and plot it

# %%
# Import the modules we will use

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import dataretrieval.nwis as nwis

# %%
# Set the file name and path to where you have stored the data

station_id1 = "09506000"
station_id2 = "09401260"
station_id3 = "09401110"

data1 = nwis.get_record(sites=station_id1, service='dv', start='2010-01-01', end='2021-10-18', parameterCd='00060')
data2 = nwis.get_record(sites=station_id2, service='dv', start='2010-01-01', end='2021-10-18', parameterCd='00060')
data3 = nwis.get_record(sites=station_id3, service='dv', start='2010-01-01', end='2021-10-18', parameterCd='00060')

data1.columns = ['flow', 'agency_cd', 'site_no']
data2.columns = ['flow', 'agency_cd', 'site_no']
data3.columns = ['flow', 'agency_cd', 'site_no']

data2.loc[data2['flow'] < 0.0,'flow'] = None 
data3.loc[data3['flow'] < 0.0,'flow'] = None 

# %%
fig, ax = plt.subplots()
ax.plot(data1.index, data1['flow'], color='black', label='09506000')
ax.plot(data2.index, data2['flow'], color='red',  label='09401260')
ax.plot(data3.index, data3['flow'], color='blue', label='09401110')
#ax.set(yscale='log')
ax.legend()
