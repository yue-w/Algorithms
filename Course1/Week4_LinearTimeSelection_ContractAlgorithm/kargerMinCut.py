# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:04:51 2019

@author: wyue
"""
import numpy as np

def readtxt(filename):
    with open(filename) as f:
        graph = f.readlines()

    for i in range(0,len(graph)):
        graph[i]=graph[i].strip('\n')
        graph[i]= graph[i].split()
        graph[i] = list(map(int,graph[i]))

    return graph
   


    
def initverticesdictionary(n):
    indexdictionary = []
    for i in range(0,n):
        indexdictionary.append(int((i+1)))
    return indexdictionary

def updateverticesdictionary(indexdictionary,vertex1,vertex2):
    """
    index of vertex1 is smaller than vertex2. vertex2 will be named to vertex1
    """
    indexdictionary[vertex2-1] = vertex1
    return indexdictionary

def getrootvertexfromverticesdictionary(indexdictionary,vertex):
    while(indexdictionary[vertex-1]<vertex):
        vertex = indexdictionary[vertex-1]
    return vertex
    

def kargeralgorithm(graph,verticesdict):
    n = len(graph)
    while n>2:
        vertex1,vertex2 = randomedge(graph)
        graph, verticesdict =  mergetwovertices(graph,verticesdict,vertex1,vertex2)
        n = n -1
        
    vertex1 = getrootvertexfromverticesdictionary(verticesdict,len(graph)-1)
    vertex2 = getrootvertexfromverticesdictionary(verticesdict,len(graph)-2)
    mincut = (len(graph[vertex1-1])+len(graph[vertex2-1])-2)/2  
    return mincut     

def cleanedges(edge_combined,verticesdict,smallervertex,largervertex):
    edges_cleaned = []
    for i in range(0,len(edge_combined)):
        vertex = edge_combined[i]
        rootvertex = getrootvertexfromverticesdictionary(verticesdict,vertex)
        if rootvertex!= smallervertex: #and vertex!= largervertex:
            #rootvertex = getrootvertexfromverticesdictionary(verticesdict,vertex)
            edges_cleaned.append(rootvertex)
    return edges_cleaned    
    
def randomedge(graph):#This is a brutal method
    alledges = []
    for i in range(0,len(graph)):       
        for j in range(1,len(graph[i][:])):
            edge = [i+1,graph[i][j]]
            alledges.append(edge)
    randindex = np.random.randint(0,len(alledges))    
    return alledges[randindex][0],alledges[randindex][1]

    
def mergetwovertices(graph,verticesdict,vertex1,vertex2):
    """
    Always keep the lower index
    """
    #smallervertex = min(vertex1,vertex2)
    #largervertex = max(vertex1,vertex2)
    index1 = getrootvertexfromverticesdictionary(verticesdict,vertex1)-1
    index2 = getrootvertexfromverticesdictionary(verticesdict,vertex2)-1
    smallerindex = min(index1,index2)
    largerindex = max(index1,index2)
    edge_small = graph[smallerindex][1:]
    edge_large = graph[largerindex][1:]
    edge_combined = edge_small+edge_large
    
    verticesdict = updateverticesdictionary(verticesdict,graph[smallerindex][0],graph[largerindex][0])
    edge_combined = cleanedges(edge_combined,verticesdict,graph[smallerindex][0],graph[largerindex][0])
    #verticesdict = updateverticesdictionary(verticesdict,graph[smallerindex][0],graph[largerindex][0])
    
    graph[smallerindex][:] = [smallerindex+1] + edge_combined
    graph[largerindex]=[] #The edges of larger vertex are stored in the smller vertex. 
    return graph, verticesdict
    

    
graphogiginal = readtxt('kargerMinCut.txt') 
graphogiginal = np.asarray(graphogiginal) 
verticesdict = initverticesdictionary(len(graphogiginal))

TotalRunning = 100
copy = graphogiginal[:]
mincut = kargeralgorithm(copy,verticesdict)
print(mincut)


