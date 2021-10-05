# Starter code for week 6 illustrating how to build an AR model 
# and plot it

# %%
# Import the modules we will use
# import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import dataretrieval.nwis as nwis
import sklearn as sklearn

# %%
# Set the file name and path to where you have stored the data

station_id = "09506000"
data = nwis.get_record(sites=station_id, service='dv', start='1989-01-01',end='2021-10-02', parameterCd='00060')
data.columns = ['flow','agency_cd','site_no']

# Expand the dates to year month day
data['year'] = data.index.year
data['month'] = data.index.month
data['day'] = data.index.day
data['dayofweek'] = data.index.dayofweek

# %% 

# 1. Timeseries of observed flow values
fig, ax = plt.subplots()
ax.plot(data.index, data['flow'], color='black',
        lw=0.5, label='daily flow')
ax.set(title="Observed Flow", xlabel="Year", 
        ylabel="Daily Avg Flow (cfs)",
        yscale='log',
        xlim=[datetime.date(2000, 1, 26), datetime.date(2021, 10, 2)])
ax.legend(frameon=False)
# an example of saving your figure to a file
fig.set_size_inches(5,4)
fig.savefig("p1.png",dpi=300)


# %%
#2 Boxplot of flows by month 
data['catdate']= 'yes'
data.loc[data.index.year>=2000,'catdate']="no"
fig, ax = plt.subplots()
ax = sns.boxplot(x="month", y="flow", hue="catdate",data=data,
                 linewidth=0.3,saturation=0.5)

ax.set(yscale='log',xlabel='Month',ylabel='Daily Observed low (cfs)')
ax.legend(title="year<2000",loc="lower left",frameon=False)

fig.set_size_inches(5,5)
fig.savefig("p2.png",dpi=300)

# %%
# 3 Plot the september flows for the last 10 years
#making a color palette to use for plotting (using the viridis one here with 12 colors)
mypal = sns.color_palette('rainbow', 12)
mypal
colpick = 0
fig, ax = plt.subplots()
for i in range(2010, 2022):
        plot_data=data[(data['year']==i) & (data['month']==10)]
        ax.plot(plot_data['day'], plot_data['flow'],
                color=mypal[colpick], label=i)
        ax.set(yscale='log',title="Observed October flow",
                xlabel='Day of the month',ylabel='Daily Observed low (cfs)')
        ax.legend(frameon=False,fontsize=6)
        colpick = colpick+1

fig.set_size_inches(5,5)
fig.savefig("p3.png",dpi=300)


# %%
# 4. fill between plot
fig, ax = plt.subplots()
y1=data.loc[(data['year']==2000) & (data['month']==9),'flow']
y2=data.loc[(data['year']==2021) & (data['month']==9),'flow']
# 2020>2021 flow
ax.plot(data.loc[(data['year']==2020) & (data['month']==9),'day'],y1,'-b',
        label='2020 flow')
ax.plot(data.loc[(data['year']==2020) & (data['month']==9),'day'],y2,'-g',
        label='2021 flow')
ax.legend()
ax.fill_between(data.loc[(data['year']==2020) & (data['month']==9),'day'],y1,y2,
                facecolor='red',alpha=0.5,linewidth=1)

ax.set(xlabel="Day of September",ylabel="Observed flow (cfs)",title="2020 vs 2021 September flow")
ax.legend(loc="lower left",frameon=False)
fig.set_size_inches(5,5)
fig.savefig("p4.png",dpi=300)

# %%
# 5. Multipanel plot histograms of flow for September and October
fig, ax = plt.subplots()
kwargs=dict(bins=30, edgecolor='grey', alpha=0.3)

m = 9
month_data = data[data['month'] == m]
ax.hist(np.log10(month_data['flow']), **kwargs,label="September")

m=10
month_data = data[data['month'] == m]
ax.hist(np.log10(month_data['flow']),**kwargs,label="October")

ax.set(xlabel='Log(Flow) (cfs)', ylabel='Count', title= "September vs October flows")
ax.legend(frameon=False)
plt.show()
fig.set_size_inches(5,5)
fig.savefig("p5.png",dpi=300)

# %%
#6. multiple hist using for loop
fig, ax = plt.subplots(1, 2)
ax= ax.flatten()  #so that we can refer to plots as ax[0]...ax[3] rather than ax[0,0]..ax[1,1]
axi = 0
month_list=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct",
                "Nov","Dec"]
for m in range(9,11):
        month_data = data[data['month'] == m]
        plot_title = month_list[m]
        ax[axi].hist(np.log10(month_data['flow']), bins=40,
           edgecolor='grey', color='purple')
        ax[axi].set(title=plot_title)
        #ax[axi].set(xlabel='Log(Flow) cfs', ylabel='count', title=plot_title)
        axi=axi+1

ax[0].set(xlabel='Log(flow) (cfs)',ylabel="Count")
ax[1].set(xlabel='Log(flow) (cfs)')
plt.show()

fig.set_size_inches(6,4)
fig.savefig("p6.png",dpi=300)


# %%
