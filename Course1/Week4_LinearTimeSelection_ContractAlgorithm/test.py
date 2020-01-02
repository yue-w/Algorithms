# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:47:44 2019

@author: wyue
"""

b = [1,2,3,4]
const = b[:]

def test(c):
    c[0] = 5
    
test(b) 
   
print(const)
print(b)