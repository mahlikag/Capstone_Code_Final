#this file is a test for the cluster python file
from Cleaning.cluster import creating_clusters
Values = creating_clusters('2007-2011.xlsx')

#creating the tests
def test_creating_clusters():
    #testing if there are 10 entries for x and y values since there are 10 cities
    assert len(Values['x'])==10 & len(Values['y'])==10 
    
    #making sure the entries for x are in list form, since for entry of x should be a list of the clusters for a specific year 
    assert isinstance(Values['x'],list)
