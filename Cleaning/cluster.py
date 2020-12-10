#importing the required packages
import pandas as pd
from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import math as m

import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter

#this function creates the clusters from DBSCAN
def creating_clusters(filename):
    #creating a list for all the years that will be ran
    Years = ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
    x = []
    y = []
    location = []
    colors = []

    #this loop will run and print for each year individually
    for yr in Years:  
        df = pd.read_excel(filename, sheet_name = eval('yr'))
        table = df.iloc[:,[0,1,2,9,13,17]]
        #removing any None values
        data = df.iloc[:,[0,9,13,17]].dropna()

        #creating the row numbers
        data['row_num'] = np.arange(len(data))

        #the average for all cities will be the sum of their clearance rates divided by three
        #in order to do this, I'm using the row number to find the appropriate values since the indexs aren't are consecutive
        avg = []
        for i in range(len(data)):
            avg.append(float((data.loc[data['row_num'] == i]['Murder/Nonnegligent Manslaughter Clearance Rate'] + data.loc[data['row_num'] == i]['Aggravated Assault Clearance Rate'] + data.loc[data['row_num'] == i]['Robbery Clearance Rate'])/3))
    
        #the averages are saved as a new column
        data['average'] = avg

        #The model for DBSCAN
        model = DBSCAN(eps = 15000, min_samples=3).fit(data)
        print(yr + 's model is: ')
        print(model)
        print()

        outliers_df = pd.DataFrame(data)
     
        #The groups of clusters
        print(yr + 's grouping is: ')
        print(Counter(model.labels_))
        print()

        t = table.dropna()
        print('The outlier cities for '+ yr +' are: ')
        print()


        #Printing each outlier one at a time
        for i in outliers_df[model.labels_==-1]['Total Population']:
            print(t.loc[data['Total Population'] == i]['City'].to_string())
     
        #Adding the x and y values and the colors to a list for the later plots
        colors.append(model.labels_)
        x.append(data.iloc[:,0])
        y.append(data.iloc[:,5])
        location.append(t.iloc[:,1] + ", " + t.iloc[:,2])
        print()
        
    values = {}
    values['colors'] = colors
    values['x'] = x
    values['y'] = y
    values['location'] = location
    return values
