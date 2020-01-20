# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:17:43 2020

@author: wyue
"""
import copy

from disjoint_set import DisjointSet

class Edge(object):
    def __init__(self,pnt1,pnt2,cost):

        self.pnt1 = pnt1
        self.pnt2 = pnt2
        self.cost = cost
        
    def __lt__(self,other):
        selfPriority = self.cost
        otherPriority = other.cost
        return selfPriority < otherPriority



class Vertices(object):
    def __init__(self,N):
        self.N = N
        self.dic = {}
    
def readtxt(filename):
    with open(filename) as f:
        graph = f.readlines()
    N = int(graph[0].strip('\n'))
    edges = []
    for i in range(1,len(graph)):
        graph[i]=graph[i].strip('\n')
        graph[i]= graph[i].split()
        graph[i] = list(map(int,graph[i]))
        edges.append(Edge(graph[i][0],graph[i][1],graph[i][2]))
    
    return N,edges

def init_vertices(vertices,edges):
    for e in edges:
        pt1 = e.pnt1
        pt2 = e.pnt2
        cost = e.cost
        #tem1 = [pt2,cost]
        if pt1 in vertices.dic:
            vertices.dic[pt1][pt2] = cost
        else: 
            vertices.dic[pt1] = {pt2:cost}

        if pt2 in vertices.dic:
            vertices.dic[pt2][pt1] = cost
        else:
            vertices.dic[pt2] = {pt1:cost}


            #vertices.dic[pt2][pt1] = cost

def init_disjointset(N,ds):
    for i in range(1,N+1):
        ds.find(i)

def union(N,k,ds,edges):
    for e in edges:
        if N>k:
            pnt1 = e.pnt1
            pnt2 = e.pnt2
            #cost = e.cost
            if False == ds.connected(pnt1,pnt2):
                N -=1
                ds.union(pnt1,pnt2)
        else:
            print('done','N=',N)
            break
    

def get_min_cost(node,clusters,vertices):
    cost_list = []
    for clust in clusters:
        mincost = float("inf")
        for v in clust:
            if v in vertices.dic[node]:
                cost = vertices.dic[node][v]
                if mincost>cost:
                    mincost = cost
        cost_list.append(mincost)
    return cost_list

   

filename = "Data/clustering1.txt" #clustering1
k = 4#Number of clustering
N,edges = readtxt(filename)
vs = Vertices(N)
init_vertices(vs,edges)
edges.sort()     
ds = DisjointSet()
init_disjointset(N,ds)
union(N,k,ds,edges)
print(list(ds.itersets()))
#cost_list = get_min_cost(1,[[3,4,5]],vs)