#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:16:19 2018

@author: akhmadsusanto
"""

import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt
 
#%matplotlib inline
 
plt.rcParams['figure.figsize']=(20,10)
plt.style.use('ggplot')

market_df = pd.read_csv('UNVR.JK2.csv', index_col='Date', parse_dates=True)

market_df.head()

df = market_df.reset_index().rename(columns={'Date':'ds', 'Close':'y'})
#df['y'] = np.log(df['y'])

df.head()

df.set_index('ds').y.plot()

model = Prophet()
model.fit(df);
future = model.make_future_dataframe(periods=366)
forecast = model.predict(future)

model.changepoints

figure = model.plot(forecast)
for changepoint in model.changepoints:
    plt.axvline(changepoint,ls='--', lw=1)


deltas = model.params['delta'].mean(0)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111)
ax.bar(range(len(deltas)), deltas)
ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.2)
ax.set_ylabel('Rate change')
ax.set_xlabel('Potential changepoint')
fig.tight_layout()

#m = Prophet(changepoints=['2014-02-03', '2014-04-11', '2014-10-16', '2014-12-15', '2015-01-30', '2015-08-24', '2015-09-29', '2016-01-21', '2016-02-11', '2018-02-08', '2018-04-06', '2018-06-29', '2018-10-29', '2014-04-03', '2014-07-25', '2014-12-03', '2015-02-27', '2018-01-26', '2018-09-21'])
#forecast = m.fit(df).predict(future)
#m.plot(forecast);

#figure = m.plot(forecast)
#for changepoint in m.changepoints:
#    plt.axvline(changepoint,ls='--', lw=1)
