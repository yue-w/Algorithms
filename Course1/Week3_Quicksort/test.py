# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:38:26 2019

@author: wyue
"""

def test(A):
    n = len(A)
    if n>0:
        A.pop()
        m=test(A)
        
        return n+m
    else:
        return 0
n = [1,2,3,4,5,6]    
print(test(n))
#print(test(6))