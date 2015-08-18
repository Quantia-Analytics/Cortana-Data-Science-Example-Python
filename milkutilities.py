# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:09:07 2015

@author: Steve Elston

This file contains some utility functions used in the time series 
regression analysis of the California milk produciton data. 
"""
    
def log_cols(df):
## A simple function to log base two transform the columns
## of a pandas data frame. 
    import numpy as np
    return df.apply(lambda x: np.log2(x))
     
def add_time_index(inFrame):
    import pandas as pd
    tmIndx = pd.date_range('1/1/1995', periods = 228, freq = 'M')
    colNames = list(inFrame)
    return pd.DataFrame(inFrame.values.tolist(), \
                          columns = colNames, \
                          index = tmIndx)