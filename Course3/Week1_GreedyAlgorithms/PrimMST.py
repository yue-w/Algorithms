# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 22:40:03 2020

@author: wyue
"""

import copy

class Vertex():
    def __init__(self, tail=0,edgescore=[],explored=False):
        self.explored = explored
        self.edgescore = edgescore
        self.tail = tail
        
def readtxt(filename):
    with open(filename) as f:
        graph = f.readlines()

    for i in range(0,len(graph)):
        graph[i]=graph[i].strip('\n')
        graph[i]= graph[i].split()
        graph[i] = list(map(int,graph[i]))
    return graph
      
def initvertices(N,graph):
    vertices = []
    for i in range(0,N):
        vertices.append(Vertex(i,[],False))
    
    vertices[0].explored = True
      
    for e in graph:
        v1=e[0]-1
        v2=e[1]-1
        cost=e[2]
        vertices[v1].edgescore.append([v2,cost])
        vertices[v2].edgescore.append([v1,cost])
    return vertices

def prim(vertices):
    #X is the min weightes
    W = []
    #UX is the vertices unexplored
    UX = copy.deepcopy(vertices)
    del UX[0]
    vertices[0].explored = True 

    #vindex = 0
    while UX:
        minw = 100000000
        mintail = 0
        vUX = 0
        #minhead = 0
        for v in range(len(UX)):
            tail = UX[v].tail
            edges = UX[v].edgescore          
            for e in range(len(edges)):
                head = edges[e][0]
                #weight = edges[e][1]
                if vertices[head].explored == True:#This edge cross frontier
                    weight = edges[e][1]
                    if weight < minw:
                        minw = weight
                        mintail = tail
                        vUX = v
                        #minhead = head
        vertices[mintail].explored = True
        W.append(minw)
        del UX[vUX]
    return W             
            
filename = "Data/edges.txt"   
graph = readtxt(filename)
#N is number of nodes
N = graph[0][0]
#M is number of edges
M = graph[0][1]
del graph[0]

vertices = initvertices(N,graph)

W = prim(vertices)
print(sum(W))

                
                
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    

   
