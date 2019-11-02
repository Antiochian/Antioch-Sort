# -*- coding: utf-8 -*- python3
"""
Antioch-Sort
@author: Antiochian
"""

import random
import numpy as np
import time

def antiochsort(array):
    length = max(array)+1
    bytemap = np.zeros(length,bool)
    output = []
    for k in array:
        bytemap[k] = True
    for j in range(length):
        if bytemap[j]:
            output.append(j)
    return output

def arraygenerator(n):
    #generates random array of shuffled integers from 0 to n with no repeats
    array = []
    for i in range(n):
        array.append(i)
    random.shuffle(array)
    return array

#####################################
#reused quicksort code from earlier project
def quicksort(A):
    start = 0
    end = len(A)-1
    quicksort_recursive(A,start,end)
    return A

def quicksort_recursive(A,start,end):
    if start < end:
        p_index = partition(A,start,end)
        quicksort_recursive(A,start,p_index-1)
        quicksort_recursive(A,p_index+1,end)
    else:
        return A
    
def partition(A,start,end):   
    p = end
    pivot = A[p]
    A[start], A[p] = A[p],A[start]
    b = start+1 #index of border
    for i in range(start+1,end+1):
        if A[i] < pivot:
            #put behind border
            A[b],A[i] = A[i],A[b]
            b += 1 
    A[b-1],A[start] = A[start],A[b-1]
    return b-1
#####################################
    
def tester(attempts,length):
    quicktime = []
    antiochtime = []
    for i in range(attempts):
        array = arraygenerator(length)
        tq = time.time()
        quick = quicksort(array)
        quicktime.append(time.time() - tq)
        ta = time.time()
        antioch = antiochsort(array)        
        antiochtime.append(time.time()-ta)
        if quick == antioch:
            print("OK...")
        else:
            print("Failed!!")
            print(array)
            print(quick,antioch)
            return
    #prints mean time taken (milliseconds)
    print("--------------------")
    print("QUICKSORT = ",sum(quicktime)/len(quicktime))
    print("ANTIOCHSORT = ",sum(antiochtime)/len(antiochtime))
    return
        
        