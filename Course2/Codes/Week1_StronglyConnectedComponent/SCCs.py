# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:19:39 2019

@author: wyue
"""
import copy
import numpy as np

#import sys
#sys.setrecursionlimit(5000)

class Vertex():
    def __init__(self,tail=0, heads=[], explored=False,fvalue=0,scc=0):
        self.tail = tail
        self.heads = heads
        self.explored = explored
        self.fvalue = fvalue
        self.scc = 0
        
    def gettail(self):
        return self.tail
    
    def getheads(self):
        return self.heads
    
    def addahead(self, head):
        self.heads.append(head)


def readtxt(filename):
    with open(filename) as f:
        graph = f.readlines()

    for i in range(0,len(graph)):
        graph[i]=graph[i].strip('\n')
        graph[i]= graph[i].split()
        graph[i] = list(map(int,graph[i]))

    return graph

def builddirectedgraph(txtfile):
    #This function will return a directed graph and a reversed version of the graph.
    #Datastructure of the directed graph: a list of vertices. Each vertex stores the vertices
    #it points to
    edges = readtxt(txtfile)
    #N = edges[-1][0]#Total number of vertices
    edgesarray = np.array(edges)
    N = max(edgesarray[:,0])
    #Init the N vertices
    vertices = []
    verticesRev = []#Reversed
    for i in range(0,N):
        head = []
        explored = False
        fvalue = 0
        scc = 0
        vertex = Vertex(i,head,explored,fvalue,scc)
        vertices.append(copy.deepcopy(vertex))
        verticesRev.append(copy.deepcopy(vertex))
        
    for e in edges:
        tailindex = e[0]-1
        headindex = e[1]-1
        vertices[tailindex].addahead(headindex)
        verticesRev[headindex].addahead(tailindex)
    return vertices,verticesRev

def markunexplored(vertices):
    for v in vertices:
        v.explored = False
    return vertices

def dfstopo(vertices,tailindex,curLabel):
    vertices[tailindex].explored = True
    heads = vertices[tailindex].getheads()
    for headindex in heads:
        if vertices[headindex].explored == False:
            curLabel = dfstopo(vertices,headindex,curLabel)
    vertices[tailindex].fvalue = curLabel
    curLabel -=1
    return curLabel

#Iterative implementation of dfstopo  
def dfstopoiterate(vertices,tailindex,curLabel):  
    #vertices[tailindex].explored = True
    vertexIndexStack = []
    vertexIndexStack.append(vertices[tailindex].tail)
    while len(vertexIndexStack)>0:
        vertexindex = vertexIndexStack.pop()
        if vertices[vertexindex].explored==False:
            
            vertices[vertexindex].explored=True
            heads = vertices[vertexindex].getheads()
            for head in heads:
                if vertices[head].explored==False:
                    vertexIndexStack.append(head)
                    deepest = vertexindex

    vertices[deepest].fvalue = curLabel
    curLabel -=1
    return curLabel       
    """
    
    for headindex in heads:
        if vertices[headindex].explored == False:
    """
    
    
def toposort(vertices):
    vertices=markunexplored(vertices)
    curLabel = len(vertices)
    
    for vertex in vertices:
        tailindex = vertex.tail
        if vertex.explored==False:
           curLabel = dfstopo(vertices,tailindex,curLabel) #Recursive implementation
           #curLabel = dfstopoiterate(vertices,tailindex,curLabel) #Iterative implementation
"""
def sortgraphbyfvalue(vertices):
    #Inplece rank of vertices by fvalue
    vertices.sort(key=lambda x:x.fvalue, reverse=False)
    return vertices
"""

def dfsscc(vertices,vertexindex,numSCC):
    vertices[vertexindex].explored = True
    vertices[vertexindex].scc = numSCC
    heads = vertices[vertexindex].heads
    for head in heads:
        if vertices[head].explored == False:
            dfsscc(vertices,head,numSCC)
    
    
def kosaraju(vertices,verticesRev):
    toposort(verticesRev)
    verticesRev.sort(key=lambda x:x.fvalue, reverse=False)#Sort vertices by f-value
    vertices=markunexplored(vertices)
    numSCC = 0    
    for vertex in verticesRev: #In increasing order of fvalue
        vertexindex = vertex.tail
        if vertices[vertexindex].explored == False:
            numSCC +=1
            dfsscc(vertices,vertexindex,numSCC)
    return numSCC
        
def outputscc(vertices):
    for v in vertices:
        print(v.scc)

def printfvalue(vertices):
    for i,v in enumerate(vertices):
        print(i+1,v.fvalue)
        
def sortscc(vertices,numSCC):
    #allscc = np.zeros((numSCC,2))
    allscc = np.zeros(numSCC)
    for v in vertices:
        allscc[v.scc-1] += 1 
    allscc = np.sort(allscc)
    return allscc
    
def main():
    txtfile = 'data/SCC.txt'
    vertices,verticesRev = builddirectedgraph(txtfile)
    
    #toposort(vertices)
    #printfvalue(vertices)
    
    numSCC = kosaraju(vertices,verticesRev)
    sortedSCC = sortscc(vertices,numSCC)
    print(sortedSCC[-5:])    

import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

thread = threading.Thread(target=main)
thread.start()