# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:07:13 2015

@author: jon
"""

# Tying to copy the instructions of R Programming Quiz 1
import pandas as pId
import numpy as np
from pandas import Series, DataFrame


df2 = pd.read_csv("data.csv")
Data = pd.read_csv("hw1_data.csv")

Data.ix[:2]
Data.ix[:-2]

# Question 14
Data.ix[151:152]
Data[-2:]

# Question 15
Data['Ozone'][46]
Data.ix[46, 0]

# Question 16
len(pd.isnull(Data))
pd.isnull(Data['Ozone'])
len(pd.isnull(Data['Ozone'] == True))
pd.isnull(Data['Ozone'] == True)

Data['Ozone'][Data['Ozone'].notnull()]
Data['Ozone'][Data['Ozone'].isnull()]
len(Data['Ozone'][Data['Ozone'].notnull()])
len(Data['Ozone'][Data['Ozone'].isnull()])  #this is the one
len(Data['Ozone'][pd.isnull(Data['Ozone'])]) #This also works

# Question 17
Data['Ozone'].mean()

# Question 18
Q18 = Data[(Data['Ozone'] > 31) & (Data['Temp'] > 90)]
Q18['Solar.R'].mean()

# Question 19
Q19 = Data[Data['Month'] == 6]
Q19['Temp'].mean()

Data['Temp'][Data['Month'] == 6].mean() # This also works

# Question 20
Data['Ozone'][Data['Month'] == 5].max()
Data[1,:]
