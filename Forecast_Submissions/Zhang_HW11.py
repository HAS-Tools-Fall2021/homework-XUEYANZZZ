# %%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
# netcdf4 needs to be installed in your environment for this to work
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset
from   sklearn.linear_model import LinearRegression
import datetime
import dataretrieval.nwis as nwis
# %%
# NCEP potential evaporation, precipitation, and 2-m temperature during 2021
# https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f
pevpr_path = os.path.join('..', 'data', 'pevpr.sfc.gauss.2021.nc')
temp_path = os.path.join('..', 'data', 'air.2m.gauss.2021.nc')
prate_path = os.path.join('..', 'data', 'prate.sfc.gauss.2021.nc')

pevpr = xr.open_dataset(pevpr_path)
temp = xr.open_dataset(temp_path)
prate = xr.open_dataset(prate_path)

pevpr
temp
prate

# We can inspect the metadata of the file like this:
# dataset.attrs
# dataset.values
# dataset.dims
# dataset.coords

# Now to grab out data first lets look at spatail coordinates:
prate['prate']['lat'].values.shape
# The first 4 lat values
prate['prate']['lat'].values
prate['prate']['lon'].values

# Now looking at the time;
prate["prate"]["time"].values
prate["prate"]["time"].values.shape


# Grabbing data for just one point forecast guage
# (34.448361, -111.789871)--> nearest gridcell (37.1422,247.5)
lat = 37.1422
lon = 247.5
print("Long, Lat values:", lon, lat)
temp_point = temp["air"].sel(lat=lat, lon=lon)-273.15
# 0.0864*0.408 is the unit conversion (w/m2 --> mm/day)
pevpr_point = pevpr["pevpr"].sel(lat=lat, lon=lon)*0.0864*0.408
prate_point = prate["prate"].sel(lat=lat, lon=lon)*3600*24


# %% Make a timeseries plot
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 9))
temp_point.plot.line(hue='lat',
                     marker="o",
                     ax=ax1,
                     color="grey",
                     markerfacecolor="red",
                     markeredgecolor="red")

prate_point.plot.line(hue='lat',
                      marker="o",
                      ax=ax2,
                      color="grey",
                      markerfacecolor="black",
                      markeredgecolor="black")
pevpr_point.plot.line(hue='lat',
                      marker="o",
                      ax=ax3,
                      color="grey",
                      markerfacecolor="blue",
                      markeredgecolor="blue")
ax1.set(title="Daily Meteorology Times Series \n (09506000 VERDE RIVER NEAR \
CAMP VERDE, AZ)",
        ylabel="2-m air temperature", xticklabels=[],xlabel=None)
ax2.set(title=None, ylim=(0, 60), ylabel="Precipitation (mm/day)",xticklabels=[],xlabel=None)
ax3.set(title=None, ylim=(0, 60), ylabel="Potential evaporation amount (mm/day)")

plt.show()
fig.savefig('site-forcing.jpg', dpi=350)

# %% Forecast
# Get USGS streamflow data
station_id = "09506000"
strfdata = nwis.get_record(sites=station_id, service='dv', start='1989-01-01', end='2021-11-05', parameterCd='00060')
strfdata.columns = ['flow', 'agency_cd', 'site_no']

# Generate weekly time series for prcp and streamflow during 1989-2020
W_strfdata = strfdata.resample('W').mean()
W_strfdata = W_strfdata[W_strfdata.index.year < 2021]

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

# Prediction; I did a substraction based on flow during last week
prediction = model.predict(train[['flow_tm1', 'flow_tm2']])
print(" This week mean flow is ", round(prediction[-1], 1)-100.)
print(" Next week mean flow is ", round(prediction[-1], 1)-120.)
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