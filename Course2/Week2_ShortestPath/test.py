# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:36:47 2020

@author: wyue
"""
import heapq
'''
a = [1,2]
b = [5,4,2,3,4]
for i in a:
    try:
        index = b.index(i)
        print(index)
    except ValueError:
        continue
'''

class T():
    def __init__(self,a):
        self.a = a

t1 = T(4)
t2 = T(4)
t3 = T(4)
t4 = T(4)

"""
h = [(t1.a,t1),(t2.a,t2),(t3.a,t3),(t4.a,t4)]   
h = []
h.append((t1.a,t1))
h.append((t2.a,t2))
h.append((t3.a,t3))
h.append((t4.a,t4))
#heapq.heapify(h)
"""
vt = [t1,t2,t3,t4]
h = []
for i in vt:
    v = i.a
    h.append((v,id(i),i))

heapq.heapify(h)
a = heapq.heappop(h)
print(a)
    