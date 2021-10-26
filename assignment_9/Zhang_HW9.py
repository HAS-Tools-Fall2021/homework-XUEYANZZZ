# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression
import datetime
import os
import json 
import urllib.request as req
import urllib
import dataretrieval.nwis as nwis
# %%
# Daymet data for a single pixle near this USGS site:
# Example accessing it as a csv; here, prcp with a unit (mm/day)
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.448&lon=-111.789" \
       "&vars=prcp&years=&format=csv"
data = pd.read_table(url, delimiter=',', skiprows=6)

# Drop data before 1989 so we can match the time with USGS streamflow data
data.drop(data[data['year']<1989].index,inplace=True)

# Generate datetime and set it as data.index
data['datetime'] = data['year'].astype(str)+data['yday'].astype(str)
data.set_index(data.index-3285, inplace=True)

for ii in np.arange(0,11680):
     temp = datetime.datetime.strptime(data['datetime'][ii], '%Y%j').strftime('%Y-%m-%d')
     data['datetime'][ii] = datetime.datetime.strptime(temp, '%Y-%m-%d')

data['datetime']
data.set_index(data['datetime'], inplace=True)
data.drop(columns=['datetime', 'year', 'yday'], inplace=True)
data.columns = ['prcp']
# %%
# Get USGS streamflow data
station_id = "09506000"
strfdata = nwis.get_record(sites=station_id, service='dv', start='1989-01-01', end='2021-10-23', parameterCd='00060')
strfdata.columns = ['flow', 'agency_cd', 'site_no']

# %%
# Generate weekly time series for prcp and streamflow during 1989-2020
W_prcp     = data.resample('W').mean()
W_strfdata = strfdata.resample('W').mean()
W_prcp     = W_prcp[W_prcp.index.year < 2021]
W_strfdata = W_strfdata[W_strfdata.index.year < 2021]

# Generate two y axis plot

fig, ax = plt.subplots()
ax.plot(W_strfdata.index, W_strfdata['flow'], color='red')
ax.set(ylabel = 'Streamflow (m^3/s)', yscale = 'log')

ax2 = ax.twinx()
ax2.plot(W_prcp.index, W_prcp['prcp'])
ax2.set(ylabel = 'Precipitation (mm/day)', xlabel = 'Year', ylim=(0, 20.0), 
        title = 'Weekly mean streamflow and precipitation')
ax2.invert_yaxis()

plt.show()
fig.savefig('two_yaxis_prcp_flow.jpg', dpi=300, bbox_inches='tight')
# %%
# Build an autoregressive model 
W_strfdata = strfdata.resample('W').mean()
W_strfdata['flow_tm1'] = W_strfdata['flow'].shift(1)
W_strfdata['flow_tm2'] = W_strfdata['flow'].shift(2)

# Using the entire flow data  
train = W_strfdata[2:][['flow', 'flow_tm1', 'flow_tm2']]

# Build a linear regression model
model = LinearRegression()
x = train[['flow_tm1', 'flow_tm2']] 
y = train['flow'].values
model.fit(x, y)

# Results of the model
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

#print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Prediction
prediction = model.predict(train[['flow_tm1', 'flow_tm2']])
print(" This week mean flow is ", round(prediction[-1], 1))
print(" This week mean flow is ", round(prediction[-1], 1)-50)
#
# %%
# Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots()
ax.scatter(W_strfdata['flow'][2:], prediction, marker='o', alpha=0.05,
            color='blue', label='simulated 2 lag')
ax.set(title="Linear regression flow results", xlabel="Observation (cfs)", ylabel="Simulation with 2 lag (cfs)",
       yscale='log', xscale='log', xlim=(0,15000), ylim=(0,15000))
ax.set_aspect('equal', adjustable='box')
ax.legend()
plt.show()

fig.savefig('lm.jpg', dpi=300)
# %%
