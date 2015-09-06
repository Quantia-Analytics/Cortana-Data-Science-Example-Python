# Cortana Analytics Conference Data Science Tutorial Example:   
## Forecasting with Azure ML and Python


## Overview

This repository contains Python code for a Microsoft Azure Machine Learning experiment used for the Data Science Example at the 2015 Cortana Analytics Conference. The experiment is in the [Microsoft Azure ML gallery](https://gallery.azureml.net/Experiment/c8c8fe15c4ee470685cc91d5e19c77dc). 

The Azure ML experiment illustrates the basics of building and evaluating a regression forecasting machine learning model, using Azure Machine Learning and Python. The goal of this experiment is to forecast the monthly milk production for the State of California. 

## Data

The data are contained in a .csv file. These data are derived from dairy production information published by the United States Department of Agriculture. The data set contains a  time series of dairy production data for several products, along with milk fat pricing, for 128 months.

## Code organization

The Azure ML experiment contains Python code running in several Execute Python Script modules. 

The milkutilities.py file contains utility functions used in the Execute Python Script modules. 

Two columns containing the square and cube of the month count are computed in an Execute Python Script module with the code in the milktransform2.py file. These new features are used in a polynomial regression of the time series trend.  

The code visualize.py file generates graphics for the visualization and exploration of the data set. Specifically, one can see that the time series has a strong trend. Further, these data exhibit a significant seasonal (monthly) variation. 

The milksplitdata.py file contains final bit of data munging code. This code divides the data into training and test sets. The last 12 months of milk production data are held back to test the forecasting power of our model. Note, the Split module would not work in this case, since it randomly samples the data.

The milkevaluate.py file contains code to compute summary statistics and visualize the model scoring (prediction) results.This information is used to evaluate model performance. 

The milklm.py file contain code to compute and predict (score) a Scikit-learn linear model for that model. This code is used for testing in Spyder or an IPython notebook and to explore feature selection.  


