# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:32:57 2015

@author: Steve Elston

This code creates a simple, but not very accurate, linear model and its 
predictions for testing the evaluation code. 
"""
def azure_main(frame1, frame2):
    from sklearn import linear_model
    
    X = frame2[['Month.Count', 'monthNumCubed', 'monthNumSqred', 'Month.Number']].as_matrix()
    Y = frame2['Milk.Prod'].as_matrix()
    regr = linear_model.LinearRegression(fit_intercept = False)
    regr.fit(X, Y)

    X = frame1[['Month.Count', 'monthNumCubed', 'monthNumSqred', 'Month.Number']].as_matrix()
    frame1['Predicted'] = regr.predict(X).tolist()
