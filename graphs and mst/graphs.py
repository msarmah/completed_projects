# Question: With the purpose of each function given, create graph from Linked List class.

import copy

class Graph():
    def __init__(self): # O(1)
        self.adj_list = {} # initialize it to a list
        
    def addVertex(self, data): # O(1)
        self.adj_list[data] = set() # add vertexes to a set
        
    def removeVertex(self, data): # O(N^2)
        del self.adj_list[data] # removing from the left side values 
        for key in self.adj_list:
            t_set = self.adj_list[key] # this is set of vertex (the value part)
            for t in t_set:
                l = list(t)
                if l[0] == data: # remove the vertex and all the info on edges with it
                    t_set.remove((l[0], l[1])) # remove within the set
                    break
        
    def addEdge(self, src, dest, weight = 1): #O(1)
        self.adj_list[src].add((dest, weight)) # add destination and weight of edge
        
    def addUndirectedEdge(self, A, B, weight = 1): #O(1)
        self.addEdge(A,B,weight) 
        self.addEdge(B,A,weight) # have to add in both directions
    
    def removeEdge(self,src,dest): #O(N^2)
        for key in self.adj_list:
            t_set = self.adj_list[key] # this is set of vertex (the value part)
            for t in t_set:
                l = list(t)
                if l[0] == dest and key == src: # delete only the destination and source 
                    t_set.remove((l[0], l[1]))
                    break
                
    def removeUndirectedEdge(self, A, B, weight = 1): # O(N)
        self.removeEdge(A,B,weight)
        self.removeEdge(B,A,weight) # have to delete in both directions
        
    def V(self): #O(1)
        return list(self.adj_list.keys()) # return all the vertexes 
        
    def E(self): #O(N^2)
        big_list = [] # initialize list 
        for k in self.adj_list.keys():
            s = self.adj_list[k] # gives us set
            for i in s:
                e = [k, list(i)[0], list(i)[1]] #get the vertex, the destination, weight
                big_list.append(e)
        return big_list
                
    def neighbors(self,value): #O(N)
        n =  self.adj_list[value] # tuple portion
        l = []
        for k in n: # looping through the tuples
            l.append(list(k)[0])
        return l
        
    def dft(self, src): #O(N^2)
        stack = []
        visited = []

        stack.append(src) # add all the verticies into the stack

        while len(stack) != 0:
            v = stack.pop() # pop the latest item out 

            if v not in visited:
                visited.append(v) # add popped to our visited list 

                neighbors = sorted(self.neighbors(v), reverse = True)
                # create sorted array from biggest to smallest (order in stack)

                for n in neighbors:
                    stack.append(n) # add to neighbors
        return visited
    
    def bft(self, src): #O(N^2)
        queue = []
        visited = []

        queue.append(src) # add all verticies to our queue

        while len(queue) != 0:
            v = queue.pop(0) # remove the earliest value added from the queue

            if v not in visited:
                visited.append(v)

                neighbors = sorted(self.neighbors(v), reverse = False)
                # create sorted array from smallest to biggest (order in queue)

                for n in neighbors:
                    queue.append(n)
        return visited
    
    def isDirected(self): #O(N^3)
        keys = self.adj_list.keys()
        for key in keys: # looped through dictionary keys
            for k in self.adj_list[key]:# looping through values now (if inside dictionary () you put it)
                v = list(k)[0] #tuple
                d = self.adj_list[v] # find a key that is the same as the destination
                found = True
                for j in d: # loop through the key's values from above
                    if key == list(j)[0] and list(k)[1] == list(j)[1]: # compare the source key to the destination
                        found = False
                        break
                if found == True:
                    return True    
        return False
    
    def isCyclic(self): #O(N^2)
        def inDegree0(graph,node): 
            for vertex, edgeList in graph.adj_list.items(): # the whole dictionary line
                for dest, weight in edgeList: # only the edges 
                    if node == dest:
                        return False # if node is the destination of our edge False
            return True

        if self.isDirected():
            newGraph = Graph()
            newGraph.adj_list = copy.deepcopy(self.adj_list) # make copy so it won't change

            while len(newGraph.V()) != 0: # loop through the length of the verticies
                n = None
                for node in newGraph.V():
                    if inDegree0(newGraph, node): # node is not the destination of our edge
                        n = node
                        break
                 

                if n == None:
                    return True #  node = dest making a cycle

                newGraph.removeVertex(n)

            return False

        else: # for undirected graphs 
            stack = []
            visited = []
            parent = {}

            src = self.V()[0]
            stack.append(src)
            visited.append(src)
            parent[src] = None

            while len(stack) != 0:
                v = stack.pop()

                neighbors = self.neighbors(v) # all the popped values go inside the neighbors

                if parent[v] != None:
                    neighbors.remove(parent[v]) # remove None

                for n in neighbors:
                    if n not in visited: # add it to the visited 
                        visited.append(n)
                        stack.append(n)

                        parent[n] = v
                    else: # if it is in visited then we have a cycle
                        return True
            return False
            
        
    def isConnected(self): # O(1)
        newGraph = Graph()
        newGraph.adj_list = copy.deepcopy(self.adj_list) # create a copy of the newGraph so not altered 

        src = self.V()[0] # the verticies
        
        if len(newGraph.V()) == len(self.dft(src)): # if the lengths are the same then we say all verticies connected
            return True
        return False
        
    def isTree(self): #O(1)
        if self.isConnected() == True and self.isCyclic() == False: # tree is connected and not cyclic 
            return True
        return False
        
    def printme(self): # O(N)
        for i,v in enumerate(self.adj_list):
            print(v, self.adj_list[v])  # used for testing

    def list_to_matrix(self): #list to matrix for prims; O(N^3)
        matrix = [] # create empty matrix
        vertex = self.V()

        for key in self.adj_list.keys():
            keys = self.adj_list[key] # keys equals the values 

            tmp = []

            for v in vertex:
                found = False
                for s in keys:
                    k = list(s) # create list of all the values for the key (edges)
                    if v == k[0]: # if the vertex equals the first edge
                        tmp.append(k[1]) # add the destination to the tmp
                        found = True
                        break
                if not found:
                    tmp.append(0) # add 0 to tmp
            matrix.append(tmp) # add tmp to matrix for one key line
            
        return matrix
