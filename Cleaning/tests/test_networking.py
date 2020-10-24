#testing the networking python file

#setting the needed information
import pandas as pd
filename  = '2007-2016.xlsx'
yr = '2015'

#calling the function for testing
df = pd.read_excel(filename, sheet_name = eval('yr'))
from Cleaning.networking import creating_networks

#storing the results from the called function
Network = creating_networks(df)
G = Network[0]

#creating the tests
def test_creating_networks():
    #checks to make sure the network G, is not empty and the function is correctly creating the nodes
    assert len(G.nodes())>0
