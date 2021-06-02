import networkx as nx
import numpy as np

"""
Use this script for playing around with Networkx.
"""

G = nx.Graph()
G.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])

d = {0: {1: 0}, 1: {2: 5, 3: 1}, 2: {2: 0}, 3: {3: 0}}

def tpsol(d, s=0, p=[], f=0):
    """
    Find the Trolley Problem solution given the utilitarian argument described.
    Arguments:
        d : A dictionary with a key to describe the neighbours 
            and value as a number of people trapped to each track
        s :   
    """
    return f in p and s or min(tpsol(d,s+d[f][t],p+[f],t) for t in d[f])

def tpsolnx(G, s=0, p=[], f=0):
    """
    The same but with Networkx 
    """
    return f in p and s or min(tpsolnx(G,s+G.degree[f],G.degree,t) for t in G.degree) 

tpsolnx(G)

print("edges")
print(list(G.edges)) 

print("degree")
print(G.degree[1])

