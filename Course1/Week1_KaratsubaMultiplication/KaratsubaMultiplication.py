# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:48:28 2019

@author: wyue

Input: two n-digit positive integers x and y. 
Output: the product x · y. 
Assumption: n is a power of 2.
"""
import numpy as np
import math

def getdigit(x):
    """
    get the number of digit of an integer x
    """   
    if x==0:
        return 1
    else:
        return 1+math.floor(np.log10(np.float64(x)))
        

def integertotwopart(x,m):
    """
    Input:
    x is an integer of 2m digits. n is a power of 2 
    Output:
    a is the fist m digits of the integer (left to right)
    b is the other m digits of the integer
    """
    """
    strx = str(x)
    
    a = strx[0:int(m)]
    b = strx[int(m):]
    """
    a = x//np.power(10.0,m)
    #b = 1.0*x-1.0*a*np.power(10.0,m)
    b = 0
    for i in range(0,int(m)):
        lastdigit = int(x%10)
        b += 10**i*lastdigit
        x = x//10.0
        #print(x)
    
    return a, b
    

    

def karatsuba(x,y):
    """
    It is assumed that the digits of x and y are the same
    """
    if x<10 or y<10:
        return 1.0*x*y
    #The size of the number
    m = max(getdigit(x),getdigit(y))    
    if m%2!=0:
        m=m+1
    m2 = m/2
    #karatsuba(x,y)
    firsthalf_x, secondhalf_x = integertotwopart(x,m2)
    
    firsthalf_y, secondhalf_y = integertotwopart(y,m2)
    p = firsthalf_x + secondhalf_x
    q = firsthalf_y + secondhalf_y
    ac = karatsuba(firsthalf_x,firsthalf_y)
    bd = karatsuba(secondhalf_x,secondhalf_y)
    pq = karatsuba(p,q)
    adbc = pq - ac - bd
    return 10.0**(m2*2)*ac + 10.0**m2*adbc + bd
        
#x = 3141592653589793238462643383279502884197169399375105820974944592
#print(integertotwopart(x,32))


x = 123456
y = 123456
#x=1234.0
#y=5678.0
a = karatsuba(x,y)
print(np.longdouble(a))
b = x*y 
print((a-b)/b)       
        
