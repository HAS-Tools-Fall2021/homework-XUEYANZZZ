# %% 
import pandas as pd 
import numpy as np

# %%
data = pd.read_csv('/Users/xueyanzhang/Documents/GitHub/HAS-Tools-Fall2021/Forecasting21/weekly_results/score_details.csv')


data['1wk.total'] = data.loc[:, data.columns.str[-8:] == '1wk.fcst'].sum(axis=1)
data['2wk.total'] = data.loc[:, data.columns.str[-8:] == '2wk.fcst'].sum(axis=1)
data['bonus'] = data.loc[:, data.columns.str[-5:] == 'bonus'].sum(axis=1)
data['sum'] = data.iloc[:,-3:].sum(axis=1)
# precentage
data['1wkp'] = data['1wk.total']/data.iloc[:,-3:].sum(axis=1)
data['2wkp'] = data['2wk.total']/data.iloc[:,-3:].sum(axis=1)
data['bonusp'] = data['bonus']/data.iloc[:,-3:].sum(axis=1)