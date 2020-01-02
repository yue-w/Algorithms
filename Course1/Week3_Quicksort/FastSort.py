# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def readtxt():    
    f = open('Numbers.txt', 'r')
    numbers = f.readlines()
    #numbers = numbers.strip('\n')
    numbers = list(map(lambda x: x.strip('\n'),numbers))
    numbers = list(map(int,numbers))
    f.close()   
    return numbers



"""
Partion the numbers by the first element of the numbers, noted as E
Return the modivied numbers, and a index partionindex. So that the number E has the index partionindex,
and the numbers before index partionindex is smaller than E, the numbers after index partionindex is larger than E. 
"""
def partion(numbers,startindex,endindex):
    M=endindex-startindex+1
    if M<=1: #only one number
        partionindex=startindex
    elif M==2: #two numbers. 
        partionindex=startindex
        if numbers[startindex]>numbers[endindex]:#swap
            tem = numbers[startindex]
            numbers[startindex] = numbers[endindex]
            numbers[endindex] = tem
    else:
        pivot = numbers[startindex]    
        partionindex = startindex + 1
        for j in range(startindex+1,endindex+1):
            if numbers[j]<pivot:
                tem = numbers[j]
                numbers[j] = numbers[partionindex]
                numbers[partionindex] = tem
                partionindex+=1
        tem = numbers[startindex]
        numbers[startindex] = numbers[partionindex-1]
        numbers[partionindex-1] = tem
        partionindex -= 1 
            
    return numbers, partionindex
    

"""
Count the number of comparisons in the Fastsort. 
The first element of the array as the pivot element.
"""    
def fastsort(CASE,numbers,startindex,endindex):
    M = endindex-startindex+1
    if M<=1:
        return numbers, 0
    else:
        if CASE==2: #Case 2, the last element is the pibot. Swap the last element with the first element
            tem = numbers[startindex]
            numbers[startindex] = numbers[endindex]
            numbers[endindex] = tem                     
        elif CASE==3:
            #first = numbers[startindex]
            #last = numbers[endindex]
            middleindex = math.floor((startindex+endindex)/2.0)
            #middle = numbers[middleindex]
            minv = min([numbers[startindex],numbers[middleindex],numbers[endindex]])
            maxv = max([numbers[startindex],numbers[middleindex],numbers[endindex]])
            if minv<numbers[middleindex] and numbers[middleindex]<maxv:
                tem = numbers[startindex]
                numbers[startindex]=numbers[middleindex] 
                numbers[middleindex]=tem
            elif minv<numbers[endindex] and numbers[endindex]<maxv:
                tem = numbers[startindex]
                numbers[startindex]=numbers[endindex] 
                numbers[endindex]=tem            
            
            
        numbers, partionindex = partion(numbers,startindex,endindex)
        
        numbers,comparisonsleft=fastsort(CASE,numbers,startindex,partionindex-1)#First part of numbers
        numbers,comparisonsright=fastsort(CASE,numbers,partionindex+1,endindex)#Second part of numbers
        
        newcompares = M-1   
    return numbers, comparisonsleft+comparisonsright+newcompares

CASE = 3
numbers = readtxt()
startindex = 0
endindex = len(numbers)-1
comparisons = 0

numbers,comparisons = fastsort(CASE,numbers,startindex,endindex)
print(numbers)
print("number of comparisons", comparisons)