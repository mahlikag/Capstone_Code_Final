#Mahlika George - Capstone Project

#importing the required packages
import networkx as nx
import math as m
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random as ran

#creating a function to calculate the euclidean distance of two given cities
def euclideanDistance(a,b,G):
    diff1 = float(G.nodes[a]['A_CR']) - float(G.nodes[b]['A_CR'])
    diff2 = float(G.nodes[a]['M_CR']) - float(G.nodes[b]['M_CR'])
    diff3 = float(G.nodes[a]['R_CR']) - float(G.nodes[b]['R_CR'])
    distance = m.sqrt((diff1**2) + (diff2**2) + (diff3**2))
    return distance
    
#creating a function that will create the networks
def creating_networks(df):

    #initilizaing the values
    table = df.iloc[:,[0,1,2,9,13,17]].dropna()
    states = table.iloc[:,2]
    cities = table.iloc[:,1]
    populations = table.iloc[:,0]
    Aclearance_rate = table.iloc[:,3]
    Mclearance_rate = table.iloc[:,4]
    Rclearance_rate = table.iloc[:,5]

    #creating the row numbers
    table['row_num'] = np.arange(len(table))


    #creating the graph in NetworkX
    G=nx.Graph()

    #Adding a node for each of the cities
    for x in range(len(table)):
        G.add_node(x)

    #storing the values each city will possess as a source of information
    for x in range (len(table)):
        G.nodes[x]['state'] = table.loc[table['row_num'] == x]['State']
        G.nodes[x]['city'] = table.loc[table['row_num'] == x]['City']
        G.nodes[x]['population'] = table.loc[table['row_num'] == x]['Total Population']
        G.nodes[x]['A_CR'] = table.loc[table['row_num'] == x]['Aggravated Assault Clearance Rate']
        G.nodes[x]['M_CR'] = table.loc[table['row_num'] == x]['Murder/Nonnegligent Manslaughter Clearance Rate']
        G.nodes[x]['R_CR'] = table.loc[table['row_num'] == x]['Robbery Clearance Rate']


    #running all possible combinations of nodes and calculating ther euclidean distance
    #this loop also keeps track of the distances and the combinations of nodes
    e_d = []
    combinations = []
    for i in range (len(table)):
        for j in range(len(table)-1): 
            e_d.append(euclideanDistance(i,((len(table)-1)+j+1)-(len(table)-1),G))
            combinations.append([i,((len(table)-1)+j+1)-(len(table)-1)])

    #setting the colors for the nodes        
    #color_map = ['black'] * len(table)
    n = 1
    while (nx.number_connected_components(G)!=1):
        for x in range(len(e_d)):
            a = combinations[x][0]
            b = combinations[x][1]

            #checking if the euclidean distance is less than 10
            if e_d[x] <= n:
                G.add_edge(a,b)
            
        n = n + 1
            
    #splitting the edges into groups so they can be later colored accordingly
    #low_edge_list = []
    #med_edge_list = []
    #high_edge_list = []
    #for x in G.edges:
        #if euclideanDistance(x[0],x[1],G)<=3:
            #high_edge_list.append(x)
        #if 3<euclideanDistance(x[0],x[1],G) and euclideanDistance(x[0],x[1],G)<=5:
            #med_edge_list.append(x)
        #if 5<euclideanDistance(x[0],x[1],G) and euclideanDistance(x[0],x[1],G)<=10:
            #low_edge_list.append(x)

    #labeling each city 
    labels = {i : cities.iloc[i] for i in range(0, len(cities))}
        
    return [G,labels]

def random(): 
    r = ran.randint(0,255)
    g = ran.randint(0,255)
    b = ran.randint(0,255)
    rgb = [r,g,b]
    return rgb

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def colors(t):
    color_mapped = []
    for x in range(len(t)):
        color_map = random()
        color_mapped.append(rgb2hex(color_map[0],color_map[1],color_map[2]))    
        
    return color_mapped
