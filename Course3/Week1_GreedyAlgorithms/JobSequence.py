# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:01:15 2020

@author: wyue
"""
import numpy as np
def readtxt(filename):
    with open(filename) as f:
        tasks = f.readlines()

    for i in range(0,len(tasks)):
        tasks[i]= tasks[i].strip('\n')
        tasks[i]= tasks[i].split()
        tasks[i]= list(map(float,tasks[i]))

    return tasks

def ordertaskbydiff(tasks):
    del tasks[0]
    for i, tk in enumerate(tasks[0:]):
        
        tasks[i].append(tk[0] - tk[1]) 
    
    tasks_sorted = sorted(tasks, key=lambda x:x[2], reverse=True)
    score = 0
    C = 0
    i = 0
    while i<len(tasks_sorted):
        tied = []
        tied.append(tasks_sorted[i])
        pos = i
        if i+1<len(tasks_sorted):
            while i+1<len(tasks_sorted) and tasks_sorted[i][2]==tasks_sorted[i+1][2]:
                tied.append(tasks_sorted[i+1])
                i+=1               
            tasks_sorted[pos:i+1] =  sorted(tasks_sorted[pos:i+1], key=lambda x:x[0], reverse=True) 
            for j in range(pos,i+1):
                C+=tasks_sorted[j][1]
                score += tasks_sorted[j][0]*C
            i+=1

        else:
            i+=1
    return score   
   
def ordertaskbyratio(tasks):
    del tasks[0]
    for i, tk in enumerate(tasks[0:]):        
        tasks[i].append(tk[0]/tk[1])   
        
    tasks_sorted = sorted(tasks, key=lambda x:x[2], reverse=True)   
    score = 0
    C = 0
    for tk in tasks_sorted:
        C +=tk[1]
        score += tk[0]*C
    return score

    
filename = 'Data/jobs.txt'
tasks = readtxt(filename)
score = ordertaskbydiff(tasks)
#score = ordertaskbyratio(tasks)
#tasks = np.asarray(tasks)
print(score)


   




