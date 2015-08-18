# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:41:17 2015

@author: Steve Elston

This file contains code for log transforming and scaling the 
columns of the California dairy data set. 
"""
   
def azureml_main(frame1):
    import pandas as pd
    import numpy as np
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

## Trim the month codes to 3 characters to ensure they
## are sonsistent. 
    frame1['Month'] = frame1['Month'].map(lambda x: str(x)[:3])

## Add a time index to the data frame
    frame1 = mu.add_time_index(frame1)
    
## Add a date-time type column.
#    frame1['datetime'] = frame1['Year'].apply(str)  + '-' + frame1['Month.Number'].apply(str)+ '-01'
#    frame1['datetime'] = pd.to_datetime(frame1['datetime'], format="%Y-%m-%d")
    
## Compute new columns containing the polynomial values
## of the count of months. 
    frame1['Month.Count']  =  frame1['Month.Number'] + \
                    12 * (frame1['Year'] - 1995)    
    x = frame1['Month.Count'].as_matrix()                
    frame1['monthNumSqred'] = np.power(x, 2).tolist()
    frame1['monthNumCubed'] = np.power(x, 3).tolist()    

    return frame1

