# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 21:19:13 2020

@author: wyue
"""
from disjoint_set import DisjointSet
import time  

def readtxt(filename):
    with open(filename) as f:
        graph = f.readlines()
    #N = int(graph[0].strip('\n'))
    firstline = graph[0].strip('\n').split()
    N = int(firstline[0])
    bits = int(firstline[1])
    vertices = []
    k = bits+2#2 bits for 0b
    for i in range(1,len(graph)):
        graph[i]=graph[i].strip('\n')  
        graph_str = graph[i].replace(" ","")        
        graph_bi = "0b"+graph_str
        
        rst = int(graph_bi,2)
        
        fmt = '#0'+str(k)+'b'
        rst = format(rst,fmt)#Zero padding
        vertices.append(rst)
    
    return N,bits,vertices

def init_disjointset(vertices,ds):
    for i in vertices:
        ds.find(i)

def hash_zero(vertices):
    dic_zero = {}
    for i,v in enumerate(vertices):
        if False == (v in dic_zero):
            dic_zero[v] = i
    return dic_zero        
    
def hash_one(dic0,bits):
    dic_one = {}
    for key,v in dic0.items():
        for j in range(0,bits):
            flip = modify_bit(bits,key,j)
            if False == (flip in dic_one):
                dic_one[flip] = [v]
            else:
                dic_one[flip].append(v)
    return dic_one

def hash_two(dic0,bits):
    dic_two = {}
    for key,v in dic0.items():
        for j in range(0,bits):
            for k in range(j+1,bits):
                flip = modify_bit(bits,key,j)
                flip = modify_bit(bits,flip,k)
                if False == (flip in dic_two):
                    dic_two[flip] = [v]
                else:
                    dic_two[flip].append(v)
    return dic_two
def modify_bit(bits,n,p): 
    mask = 1 << p 
    rst = int(n,2)^mask
    fmt = '#0'+str(bits+2)+'b'
    rst = format(rst,fmt)#Zero padding
    return rst
def union0(ds,vertices,dic0):
    for v,key in enumerate(vertices):
        if key in dic0:
            index = dic0[key]
            ds.union(vertices[v],vertices[index])
    
def union(ds,dic0,dic,vertices):
    #dic0 is unique vertices
    for key,v in dic0.items():
        if key in dic:
            indices = dic[key]
            for index in indices:
                ds.union(vertices[v],vertices[index])
    return ds   


filename = "Data/clustering_big.txt" #clustering_big
start_time = time.time() 
N,bits,vertices = readtxt(filename)
ds = DisjointSet()
init_disjointset(vertices,ds)

dic_zero = hash_zero(vertices)
#Cluster all vertices with distance zero
#union0(ds,vertices,dic_zero)

dic_one = hash_one(dic_zero,bits)
#Cluster all vertices with distance one
ds = union(ds,dic_zero,dic_one,vertices)

dic_two = hash_two(dic_zero,bits)
#Cluster all vertices with distance two
ds = union(ds,dic_zero,dic_two,vertices) 

clusters = list(ds.itersets())
print("Number of clusters:", len(clusters))
print("Runtime: --- %s seconds ---" % (time.time() - start_time))