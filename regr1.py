#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:45:30 2018

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
