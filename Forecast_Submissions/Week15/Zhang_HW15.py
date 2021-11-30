# %%
import numpy as np
import pandas as pd
from   sklearn.linear_model import LinearRegression
import datetime
# %%
# Get USGS streamflow data
filepath = './streamflow_week15.txt'

# Read the data into a pandas dataframe
strfdata = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )
strfdata.set_index('datetime', inplace=True)

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

# %%
