import numpy as np
import random

"""
We implement a basic, simplified utilitarian method of reasoning to solve
the trolley problem. The problem consists of deciding whether to pull
a lever that would change the track of an incoming train such that it would
kill fewer people tied to the tracks. 
Given a directed graph as an input file and a nonnegative integer attached to
each edge (the number of people tied to that track). Still, this argument has
its limits. It assumes each human has the same utility and that changing the
path the train would take is completely within our control. It also doesn't 
address the question of what caused the scenario to begin with (e.g., how 
did you find yourself in a case in which you have to resort to pullling a
lever to save the lives of others?)
"""

"""
Given input graph of the trolley problem, calculate the optimal route that kills the 
fewest number of people. The input d is a dictionary to describe the neighbors 
and number of people trapped to each track. The dictionary should use each key as the node 
and entries as the neighbors and number of people on the track connecting that node to neighbor.
"""

y = lambda d,s=0,p=[],f=0:f in p and s or min(y(d,s+d[f][t],p+[f],t)for t in d[f])
d = {0: {1: 0}, 1: {2: 5, 3: 1}, 2: {2: 0}, 3: {3: 0}}


