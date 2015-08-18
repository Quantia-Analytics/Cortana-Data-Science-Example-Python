# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:29:52 2015

@author: Steve Elston

This file contains code for the evaluation of the California milk
production data time series regression. 
"""
def rmse(Resid):
    import numpy as np
    resid = Resid.as_matrix()
    length = Resid.shape[0]
    return np.sqrt(np.sum(np.square(resid)) / length)
    
    
def azureml_main(frame1):
# Set backend    
    import matplotlib
    matplotlib.use('agg')   
    
    import matplotlib.pyplot as plt 
    import milkutilities as mu
    import statsmodels.api as sm
    import pandas as pd
    
    Azure = False

## Add a time index to the data frame
    frame1 = mu.add_time_index(frame1)

## Compute the residuals    
    frame1['Resid'] = frame1['Milk.Prod'] - frame1['Scored Labels']
    
    fig1 = plt.figure(1, figsize = (12,9))
    ax = fig1.gca()
    frame1[['Milk.Prod', 'Scored Labels']].plot(ax = ax)
    plt.xlabel("Date")
    plt.ylabel("Log CA milk production")
    plt.title("Log of milk produciton vs. date")
    plt.show()
    if(Azure == True): fig1.savefig('scatter1.png')
      
    fig2 = plt.figure(1, figsize = (12,9))
    fig2.clf()
    ax = fig2.gca()
    frame1['Resid'].plot(ax = ax)
    plt.xlabel("Date")
    plt.ylabel("Residuals of linear model")
    plt.title("Residuals of linear model vs. date")
    plt.show()
    if(Azure == True): fig2.savefig('scatter2.png')
    
    
    fig3 = plt.figure(1, figsize = (12,9))
    fig3.clf()
    ax = fig3.gca()
    frame1.boxplot( column = ['Resid'], ax = ax,
                   by = ['Month.Number','Month'])
    plt.xlabel("Month of year")
    plt.ylabel("Residuals of linear model")
    plt.title("Residuals of linear model by Month")
    plt.show()  
    if(Azure == True): fig3.savefig('scatter3.png')
  
  ## QQ Normal plot of residuals    
    fig4 = plt.figure(figsize = (12,6))
    fig4.clf()
    ax = fig4.gca()
    sm.qqplot(frame1['Resid'], ax = ax)
    ax.set_title('QQ Normal plot of residuals')
    if(Azure == True): fig4.savefig('plot4.png')

## Histograms of the residuals
    fig5 = plt.figure(figsize = (12,6))
    fig5.clf()
    fig5.clf()
    ax = fig5.gca()
    ax.hist(frame1['Resid'].as_matrix(), bins = 40)
    ax.set_xlabel("Model residuals")
    ax.set_ylabel("Density")
    ax.set_title("Histogram of residuals")
    if(Azure == True): fig5.savefig('plot5.png')

## Compute a data frame with the rms errors for the model    
    out_frame = pd.DataFrame({ \
      'rmse_Overall' : [rmse(frame1['Resid'])], \
      'rmse_test' : [rmse(frame1.ix['2013-01-31':, 'Resid'])] }) 
    
    return out_frame
