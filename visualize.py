# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 07:57:44 2015

@author: Steve Elston

This file contains code to visualize the CA Milk data set
"""

def azureml_main(frame1):
# Set backend    
    import matplotlib
    matplotlib.use('agg')   
    
    import matplotlib.pyplot as plt 
    import milkutilities as mu
    from sklearn import linear_model
    
    Azure = False
    
    X = frame1[['Month.Count', 'monthNumCubed']].as_matrix()
    Y = frame1['Milk.Prod'].as_matrix()
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)

    frame1['Predicted'] = regr.predict(X).tolist()
    frame1['Resid'] = frame1['Milk.Prod'] - frame1['Predicted']

## Add a time index to the data frame
    frame1 = mu.add_time_index(frame1)
    
    fig1 = plt.figure(1, figsize = (12,9))
    ax = fig1.gca()
    frame1[['Milk.Prod', 'Predicted']].plot(ax = ax)
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
  
    
    return frame1

