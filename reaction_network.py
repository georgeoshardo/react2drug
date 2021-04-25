#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Just trying some stuff for HackMed 2021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyvis.network import Network
import networkx as nx
import re
from itertools import product, combinations
from random import choice




adjacency_list = pd.read_csv('adjacency_list.csv')


for t in range(len(adjacency_list)):
    
    if adjacency_list['reactant_name'][t] is np.nan:
        adjacency_list['reactant_name'][t]=str(adjacency_list['ChEBI_reactant'][t])
        
    else:
        adjacency_list['reactant_name'][t]=str(adjacency_list['reactant_name'][t])
        
        
for w in range(len(adjacency_list)):
        
    if adjacency_list['product_names'][w] is np.nan:
        adjacency_list['product_names'][w]=str(adjacency_list['ChEBI_product'][w])
        
    else:
        adjacency_list['product_names'][w]=str(adjacency_list['product_names'][w])


#assign 7 random features 
features=list(np.random.randint(low=1,high=8,size=len(adjacency_list)))


colordic={1:'red',2:'blue',3:'green',4:'gold',5:'magenta',6:"coral",7:"cyan"}
adjacency_list['color']=[colordic.get(n,n) for n in features]


#using the adjacency list to create a graph

#mapped_data=adjacency_list.sample(frac=0.05)
#G=nx.from_pandas_edgelist(mapped_data, 'reactant_name', 'product_names',edge_attr='color')

G=nx.from_pandas_edgelist(adjacency_list, 'reactant_name', 'product_names',edge_attr='color')

g = Network(height=800, width=800)
g.toggle_hide_edges_on_drag(False)
g.barnes_hut()
g.from_nx(G)
g.show("ex.html")


#Look for the path to the source product and limit the path to a desired nuber of steps

T=nx.dfs_tree(G, source='Calcifediol anhydrous',depth_limit=2)

tg = Network(height=800, width=800)
tg.toggle_hide_edges_on_drag(False)
tg.barnes_hut()
tg.from_nx(T)
tg.show("path.html")



    


