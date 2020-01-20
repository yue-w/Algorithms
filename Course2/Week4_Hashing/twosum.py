# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:37:33 2020

@author: wyue
"""

def readtxt(filename):
    with open(filename) as f:
        numbers = f.readlines()

    for i in range(0,len(numbers)):
        numbers[i]=int(numbers[i].strip('\n'))
        
    return numbers

filename = 'Data/2sum.txt'
numbers = readtxt(filename)




"""
Old method. Long running time, but the answer is correct.
nhash = {i:1 for i in numbers}
result = []
for t in range(-10000,10001):
    for x in numbers:
        y = t - x
        yp = nhash.get(y)
        if yp and y!=x:
            #result.append([x,y])
            result.append(t)

rhash = {i:1 for i in result}
print(len(rhash))            
"""     

result = {}

numbers.sort()

T_lo = -10000
T_hi = 10000
    
lo = 0
hi = len(numbers)-1 
while hi>lo:
    low = numbers[lo]
    high = numbers[hi]
    sumv = low+high
    if sumv<T_lo:
        lo += 1
        continue
    elif sumv>T_hi:
        hi -= 1
        continue
    else:
        inlo = lo
        sumv = numbers[inlo]+numbers[hi]
        while sumv>=T_lo and sumv<=T_hi:            
            result[sumv] = 1
            inlo +=1
            if numbers[inlo]==numbers[hi]:
                break
            sumv = numbers[inlo]+numbers[hi]
        hi -= 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    