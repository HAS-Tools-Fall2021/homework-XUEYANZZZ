# Starter code for week 7 illustrating how to build an AR model 
# and plot it

# %%
# Import the modules we will use
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import datetime
import dataretrieval.nwis as nwis

# %%
# Set the file name and path to where you have stored the data

station_id = "09506000"
data = nwis.get_record(sites=station_id, service='dv', start='1989-01-01', end='2021-10-16', parameterCd='00060')
data.columns = ['flow', 'agency_cd', 'site_no']

# Check data info
data.head(5)
data.columns
data.index

# Information required to generate 1-week and 2-week forecast
forecast = np.zeros((3,2))

# %% Time series of October flow
# Plot 1: the October flows for the last 10 years  
# Making a color palette to use for plotting (using the viridis one here with 12 colors)

mypal = sns.color_palette('rainbow', 12)
mypal
colpick = 0
fig, ax = plt.subplots()

for i in range(2010, 2022):

        plot_data = data[(data.index.year == i) & (data.index.month == 10)]

        ax.plot(plot_data.index.day, plot_data['flow'],
                color=mypal[colpick], label=i)
        ax.set(yscale='log', title="Observed October flow (2010-2021)", 
                xlabel='Day of the month', ylabel='Daily Observed low (cfs)')
        ax.legend(frameon=False, fontsize=6)

        colpick = colpick+1

ax.vlines(x=[17, 23], ymin=0, ymax=2000, colors='k', label='day 17-23')
ax.set(ylim=(0, 2000), xlim=(1, 31))
ax.legend(frameon=False, fontsize=6)

# Save the first plot in current directory

fig.set_size_inches(5, 5)
fig.savefig("p1.png", dpi=300)

# save values for forecast
forecast = np.zeros((4,2))

# %% Time series of 3rd and 4th week mean flow during Ocober (1989-2020)
def week_mean(data, strday, endday, month):
        ''' Calculate Time series of 7-day averages

        Inputs
        ------------
        data: your pandas data frame with datetime as row index
        strday: starting day
        endday: ending day
        month: the selected month

        Outputs
        ------------
        A time series of 7-day flow averages in the selected month
        '''
        month_data = data[(data.index.month == month) &
                      (data.index.day >= strday) & (data.index.day <= endday)]
        result = month_data.groupby(month_data.index.year).mean()
        return result


week1_mean = week_mean(data, 17, 23, 10)
week2_mean = week_mean(data, 24, 30, 10)

fig, ax = plt.subplots()
ax.plot(week1_mean.index, week1_mean['flow'],  label="1 week mean")
ax.plot(week2_mean.index, week2_mean['flow'],  label="2 week mean")

ax.legend(frameon=False)
ax.set(xlabel='Year', ylabel='Observed flow (cfs)',
        title="3rd and 4th week mean flow during Ocober", ylim=(0, 650))

plt.show()
fig.set_size_inches(5, 5)
fig.savefig("p2.png", dpi=300)

# Save multi-year averages of 3rd and 4th week mean flow
forecast[0, 0] = week1_mean.mean()
forecast[0, 1] = week2_mean.mean()

# Save multi-year median of 3rd and 4th week mean flow
forecast[1, 0] = week1_mean.median()
forecast[1, 1] = week2_mean.median()

# %% October during 2021

fig, ax = plt.subplots()
ax.plot(data.tail(16).index.day, data.tail(16)['flow'], color='k')
ax.set(xlabel='Day', ylabel='Observed flow (cfs)', title='2021 October flow', xlim=(1, 16))
ax.legend(frameon=False)

fig.set_size_inches(5, 5)
fig.savefig("p3.png", dpi=300)

# Land water memory dervied from first 16 days of this October
forecast[2, 0] = data.tail(16)['flow'].mean()*0.15
forecast[2, 1] = data.tail(16)['flow'].mean()*0.10
# %% Final 1 week and 2 week forecast
# I parameterized weekly forecas as a function of muli-year
# average of weekly mean of he forecast week, median of
# weekly mean of he forecast week, and daily flow mean of this October.

forecast[3, 0] = 0.35*forecast[0, 0]+0.55*forecast[1, 0]+0.1*forecast[2, 0]
forecast[3, 1] = 0.35*forecast[0, 1]+0.55*forecast[1, 1]+0.1*forecast[2, 1]

print(' 1 week flow forecast is', round(forecast[3, 0], 1))
print(' 2 week flow forecast is', round(forecast[3, 1], 1))
# %%
