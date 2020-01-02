# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:26:13 2019

@author: wyue
"""

import math



def merge(leftintegers,rightintegers):
    L = len(leftintegers)
    R = len(rightintegers)
    M = L+R
    combined = [0]*M
    i=0
    j=0
    
    for k in range(0,M):
        if i==L:
            combined[k]=rightintegers[j]
            j=j+1
        elif j==R:
            combined[k]=leftintegers[i]
            i=i+1
        else:
            if leftintegers[i]<rightintegers[j]:
                 combined[k]=leftintegers[i]
                 i=i+1
            else:
                 combined[k]=rightintegers[j]
                 j=j+1
            
    return combined   
        
        
def mergesort(numbers):
    N = len(numbers)
    if N==1:
        return numbers
    else:
        NLeft=math.ceil(N/2)
        #NRight=N-N2     
        sortedleft=mergesort(numbers[0:NLeft])
        sortedright=mergesort(numbers[NLeft:N])
        sortednumbers = merge(sortedleft,sortedright)
        return sortednumbers
 
    
def readtxt():    
    f = open('IntegerArray.txt', 'r')
    numbers = f.readlines()
    #numbers = numbers.strip('\n')
    numbers = list(map(lambda x: x.strip('\n'),numbers))
    numbers = list(map(int,numbers))
    f.close()   
    return numbers
    
integers = readtxt()

#Total number of integers
integers = readtxt()
b = mergesort(integers)
print(b)    