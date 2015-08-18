# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:41:17 2015

@author: Steve Elston

This file contains code for creating a training data set for a 
time series regression of the California milk produciton data.  
"""
    
## This code adds a time index to the pandas dataframe.    
def azureml_main(frame1):
    import pandas as pd
    import milkutilities as mu
    import os.path
 
## If not in the Azure environment, read the data from a csv 
## file for testing purposes. Use os.path.join to create an
## OS independent way to create the full path, which should
## work on Windows, Mac, and Linux.   
    Azure = False  
    if(Azure == False):
        pathName = "C:/Users/Steve/Documents/AzureML/Data Sets/CA_Milk"
        fileName = "cadairydata.csv"
        filePath = os.path.join(pathName, fileName)
        frame1 = pd.read_csv(filePath)

## Add a time index to the data frame
    frame1 = mu.add_time_index(frame1)
    
## Cut the last 12 months off the end of the 
## data frame using pandas time series indexing. 
    frame2  =  frame1[:'2013-01-01']     

    return frame2

