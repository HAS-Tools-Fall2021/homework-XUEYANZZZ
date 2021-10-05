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

# %% Histograms used to generate flow during a selected month and years

def generate_hist(data, stryear, endyear, month, yourtitle, figurename):

        fig, ax = plt.subplots()
        kwargs = dict(bins=30, edgecolor='grey', alpha=0.3)

        month_data = data[(data['month'] == month) & \
                        (data['year'] >= stryear) & (data['year'] <= endyear)]

        ax.hist(np.log10(month_data['flow']), **kwargs, label="October")

        # Add a vertical line with mean flow

        ax.vlines(x=np.log10(month_data['flow']).mean(), ymin=0, ymax=200, colors='k', label='October mean')
        print(month," mean = ",10**(np.log10(month_data['flow']).mean()))
        ax.legend(frameon=False)
        ax.set(xlabel='Log(Flow) (cfs)', ylabel='Count', title=yourtitle, ylim=(0,200))

        plt.show()

        fig.set_size_inches(5, 5)
        fig.savefig(figurename, dpi=300)

# %%
# Set the file name and path to where you have stored the data

station_id = "09506000"
data = nwis.get_record(sites=station_id, service='dv', start='1989-01-01', end='2021-10-09', parameterCd='00060')
data.columns = ['flow','agency_cd','site_no']

# Expand the dates to year month day

data['year'] = data.index.year
data['month'] = data.index.month
data['day'] = data.index.day
data['dayofweek'] = data.index.dayofweek

# check data info
data.head(5)
data.columns
data.index

# %% Time series of October flow
# Plot 1: the October flows for the last 10 years given climate change
# making a color palette to use for plotting (using the viridis one here with 12 colors)

mypal = sns.color_palette('rainbow', 12)
mypal
colpick = 0
fig, ax = plt.subplots()

for i in range(2010, 2022):

        plot_data = data[(data['year'] == i) & (data['month'] == 10)]

        ax.plot(plot_data['day'], plot_data['flow'],
                color=mypal[colpick], label=i)
        ax.set(yscale='log', title="Observed October flow", 
                 xlabel='Day of the month', ylabel='Daily Observed low (cfs)')
        ax.legend(frameon=False, fontsize=6)

        colpick = colpick+1

ax.vlines(x=[10,16], ymin=0, ymax=2000, colors='k', label='day 10-16')
ax.set(ylim=(0,2000), xlim=(1, 31))
ax.legend(frameon=False, fontsize=6)

# Save the first plot in current directory

fig.set_size_inches(5, 5)
fig.savefig("p1.png", dpi=300)


# %% Histogram of October flow during all years (1989-2021)
# Plot 2

generate_hist(data=data, stryear=1989, endyear=2021, month=10, 
              yourtitle="October flow", figurename="p2.png")



# %% Weekly mean during day 10-16 of October during all past years

sep_data = data[(data['month'] == 10) & (data['day'] >= 10) & (data['day'] <= 16) 
        & (data['year'] <= 2020) ].groupby('year').mean()

fig, ax = plt.subplots()
ax.plot(sep_data.index, sep_data['flow'], color='k', label='Weekly flow')
ax.hlines(y=sep_data['flow'].mean(), xmin=1989, xmax=2020, colors='r', label='Multi-year mean')
ax.text(1995, 175, 'mean = 127.5 cfs', fontsize=12)
ax.set(xlabel='Year', ylabel='Weekly mean flow (cfs)', xlim=(1989, 2020))
ax.legend(frameon=False)

fig.set_size_inches(5, 5)
fig.savefig("p3.png", dpi=300)
# %%
