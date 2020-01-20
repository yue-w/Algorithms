# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:52:33 2020

@author: wyue
"""
import heapq

def readtxt(filename):
    with open(filename) as f:
        numbers = f.readlines()

    for i in range(0,len(numbers)):
        numbers[i]=int(numbers[i].strip('\n'))
        
    return numbers

    
def getmedian(medians,hs,hl,new_number):
    """
    hs is the heap stores the smaller half of the numbers given so far, it is a max heap
    hl is ... larger half ..., it is a min heap
    """
        
    #The largest number in hs
    max_hs = -hs[0]
    #The smallest number in hl
    min_hl = hl[0]
    
    if new_number<max_hs:#Number smaller than max of smaller half go to smaller half
        heapq.heappush(hs,-new_number)
        #medians.append(max_hs)
    elif new_number>min_hl:#Number larger than min of larger half go to larger half
        heapq.heappush(hl,new_number)
        #medians.append(min_hl)
    else:#number between max of smaller half and max of larger half go to smaller half
        heapq.heappush(hs,-new_number)
        
        
    ##First make shure the difference between length of two heaps less than 2
    len_hs = len(hs)
    len_hl = len(hl)
    diff = len_hs - len_hl
    if diff==-2:#Move the smallest number from hl to hs. 
        min_hl = heapq.heappop(hl)
        heapq.heappush(hs,-min_hl)
        medians.append(-hs[0])#The two heaps are now have same length. max in smaller half is median
    elif diff==2:#Move the largest number in hs to hl
        max_hs = heapq.heappop(hs)
        heapq.heappush(hl,-max_hs)
        medians.append(-hs[0])#The two heaps are now have same length. max in smaller half is median
    elif diff==-1:#Larger half has 1 more element. The min in larger half is median
         medians.append(hl[0])
    elif diff==1 or diff==0:#Smaller half has 1 more element. The max in smaller half is median
         medians.append(-hs[0])       
    else:
        print("ERROR:Two Heaps unbalanced!")

#




filename = 'Data/median.txt'
numbers = readtxt(filename)
minfirsttwo = min(numbers[0],numbers[1])
medians = [numbers[0],minfirsttwo]
hs=[-minfirsttwo]
hl=[max(numbers[0],numbers[1])]
for i in numbers[2:]:
    getmedian(medians,hs,hl,i)
    
result = sum(medians)
print(result)
  
