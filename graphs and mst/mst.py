# Question: Use graph class to implement Prim's MST algorithm.

import json
import numpy
from graph import Graph

def prim(graph): # O(N^3)
    INF = 99999999999999
    G = graph.list_to_matrix() 
    N = len(G) # length of our matrix
    start_node = [0] * N
    
    no_edge = 0
    
    start_node[0] = True

    vertex = graph.V()
    edges = []

    while no_edge < N-1: # finding the smallest weight edge to add to our vertex
        minimum = INF
        a = 0
        b = 0
        for m in range(N): 
            if start_node[m]: # the start node now starts with the first m in range
                for n in range(N): 
                    if ((not start_node[n]) and G[m][n]): # start_node False and matrix two coordinates
                        if minimum > G[m][n]: # this is the new minimum
                            minimum = G[m][n]
                            a  = m
                            b = n
        start_node[b] = True
        edges.append([vertex[a],vertex[b],G[a][b]]) # append these edges to our edges list
        no_edge += 1 # loop through and increase until while loop goes through all matrix
    return edges 
                            

def runPrim(): #O(N^2)
    with open("data.json","r") as f:
        data = json.load(f)

    g = Graph()
    
    for city in list(data.keys()):
        g.addVertex(city) # add city that we want to connect

    for city1 in g.V():
        for city2 in g.V(): # go through matrix to find
            loc1x = data[city1][0]
            loc1y = data[city1][1]
            loc2x = data[city2][0]
            loc2y = data[city2][1] # all of these are the distances between the cities from their coordinates
            cost = numpy.round(numpy.sqrt(numpy.square(loc1x-loc2x)+numpy.square(loc1y-loc2y)),2)#math
            g.addEdge(city1, city2, cost) # add the edge and cost

    g.printme()
    f.close()
    return prim(g)
        
