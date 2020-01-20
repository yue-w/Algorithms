# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:29:54 2020

@author: wyue
"""
import heapq
import copy

LARGE=1000000

class Vertex():
    def __init__(self,tail=0,heads_dis=[],mindistance=LARGE,heapindex=-1,explored=False):
        self.tail = tail
        self.heads_dis = heads_dis
        self.mindistance = mindistance
        self.heapindex = heapindex
        self.explored = explored
        
def readtxt(filename):
    with open(filename) as f:
        graph = f.readlines()

    for i in range(0,len(graph)):
        graph[i]=graph[i].strip('\n')
        graph[i]= graph[i].split()
        #graph[i] = list(map(int,graph[i]))

    return graph

def parsealine(vertex,oneline):
    
    vertex.tail = int(oneline[0])
    for i in range(1,len(oneline)):
        val = oneline[i].split(',')
        val = tuple(map(int,val))
        vertex.heads_dis.append(val) 
    return vertex

def graphtovertices(graph):
    vertices = []
    for i in graph:
        vertex = Vertex(heads_dis=[])
        vertex = parsealine(vertex,i)
        vertices.append(vertex)
    
    return vertices

def mapheapindex(vertices,unexplored):
    """
    Store the index in heap in the graph
    the index is before the min value is popped
    """
    for heapindex,v in enumerate(unexplored):
        vertexindex = v[2].tail-1
        vertices[vertexindex].heapindex = heapindex

def updatedistance(indexV,vertices,unexplored):
    heads_dis = vertices[indexV].heads_dis
    for edge in heads_dis:
        headindex = edge[0]-1
        distance = edge[1]
        heapindex = vertices[headindex].heapindex-1#min is removed, so index minus 1
        if vertices[headindex].explored == False:
            minv = min(vertices[indexV].mindistance+distance,unexplored[heapindex][2].mindistance)
            unexplored[heapindex][2].mindistance = minv
            newtuple = (minv,id(unexplored[heapindex]),unexplored[heapindex][2])
            unexplored[heapindex]= newtuple
    
    heapq.heapify(unexplored) 
    mapheapindex(vertices,unexplored)
    



    
def dijkstra(startvertex,vertices,unexplored):    
    for i in range(1,len(vertices)):
        #mindis = copy.deepcopy(vertices[i].mindistance)
        #v = copy.deepcopy(vertices[i])
        unexplored.append((vertices[i].mindistance,id(vertices[i]),vertices[i]))
    
    heapq.heapify(unexplored)
    mapheapindex(vertices,unexplored)
    while unexplored: #When there are vertices have not been computed
        #nearesttuple = heapq.heappop(unexplored)
        nearesttuple = unexplored.pop(0)
        distanceV = nearesttuple[0]
        indexV = nearesttuple[2].tail-1
        vertices[indexV].mindistance = distanceV
        vertices[indexV].explored = True
        ##update heap to maintain invariant
        updatedistance(indexV,vertices,unexplored)

def initmindis(vertices):
    vertices[0].mindistance = 0
    vertices[0].explored = True
    for edge in vertices[0].heads_dis:
        head = edge[0]
        dis = edge[1]
        vertices[head-1].mindistance = dis
     
    return vertices   
    
path = 'data/Data.txt'
graph = readtxt(path)
vertices = graphtovertices(graph)

vertices = initmindis(vertices)
startvertex =  vertices[0] 
unexplored = []
dijkstra(startvertex,vertices,unexplored)

tenvertices = [7,37,59,82,99,115,133,165,188,197]
for v in tenvertices:
    print(vertices[v-1].mindistance)




