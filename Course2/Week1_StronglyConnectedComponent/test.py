# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:55:45 2019

@author: wyue
"""

'''
x = [1,2,3,4]

def testf(x):
    x.pop()
    return x

y = [4,3,2,1]
z = testf(y)    

print('x',x)
print('y',y)
print('z',z)   

####################
class A():
    def __init__(self, age, name):
        self.age = age
        self.name = name

a1 = A(10,'Ten')
a2 = A(5,'Five')
a3 = A(2,'Two')
a4 = A(30,'Thirty')
people = [a1,a2,a3,a4]

print('Before Rank')    
for p in people:
    print(p.name, p.age)

#Inplace rank
people.sort(key=lambda x: x.age, reverse=False)
print('In place rank Rank')    
for p in people:
    print(p.name, p.age)

class A():
    def __init__(self,name):
        self.name = name

a = A("originalname")
people1 = []
people2 = []
people1.append(copy.deepcopy(a))
people2.append(copy.deepcopy(a))
people1[0].name = "changed"

'''
import numpy as np

a = []
print(len(a))
a.append(1)
a.append(2)
print(a.pop())
print(a.pop())


    