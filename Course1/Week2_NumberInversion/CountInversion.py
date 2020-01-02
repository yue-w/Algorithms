# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:11:23 2019

@author: wyue
"""
import math
#import mergesort as ms

def readtxt():    
    f = open('IntegerArray.txt', 'r')
    numbers = f.readlines()
    #numbers = numbers.strip('\n')
    numbers = list(map(lambda x: x.strip('\n'),numbers))
    numbers = list(map(int,numbers))
    f.close()   
    return numbers


def sortandcountsplitinversion(integers_left_sorted,integers_right_sorted):
    L = len(integers_left_sorted)
    R = len(integers_right_sorted)
    M = L+R
    combinedintegers = [0]*M
    i=0
    j=0
    splitInv = 0
    for k in range(0,M):
        if i==L:
            combinedintegers[k] = integers_right_sorted[j]
            j=j+1
        else:
            if j<R:
                if integers_left_sorted[i]<=integers_right_sorted[j]:
                    combinedintegers[k] = integers_left_sorted[i]
                    i=i+1 
                elif integers_left_sorted[i]>integers_right_sorted[j]:
                    combinedintegers[k] = integers_right_sorted[j]
                    splitInv = splitInv+L-i
                    j=j+1
            else:
                combinedintegers[k] = integers_left_sorted[i]
                i=i+1                 
            
    return combinedintegers, splitInv
      
    
def sortandcountinv(integers):
    
    #Total number of integers
    N = len(integers)
    
    if N<2: #base case
        return integers, 0
    else:
        NLeft = math.ceil(N/2)
        #NRight = N-NLeft
        integers_left = integers[0:NLeft]
        integers_right = integers[NLeft:N]
        integers_left_sorted, leftInv = sortandcountinv(integers_left)
        integers_right_sorted, rightInv = sortandcountinv(integers_right)
        integers_sorted, splitInv = sortandcountsplitinversion(integers_left_sorted,integers_right_sorted)
        
        return integers_sorted, leftInv+rightInv+splitInv
        
integers = readtxt()
integers_sorted, inver=sortandcountinv(integers)   
print(integers_sorted)
print(inver)
    
  
    

