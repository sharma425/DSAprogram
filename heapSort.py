# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:12:48 2021

@author: Keshav
"""

import random
import timeit
import matplotlib.pyplot as plt

def heapify(A,n,k):
    largest = k             #Initialize largest
    l=2*k+1                 #left 
    r=2*k+2                 #right
    
    #if left child is larger than root
    if l<n and A[largest]<A[l]:
        largest = l
        
    #if right child larger than root
    if r<n and A[largest]<A[r]:
        largest = r
        
    #if largest is not root
    if largest != k :
        A[k],A[largest]=A[largest],A[k]
        heapify(A, n, largest)          #resursive calling

def maxHeap(A):         #for max heap
    for i in range(len(A)//2-1,-1,-1):
        heapify(A, len(A), i)
        
        
def heapSort(A):
    maxHeap(A)
    #extraction element one by one
    for i in range(len(A)-1,-1,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A, i, 0)
     
        

N = int(input("Enter the number of elements : "))
A=[]
for i in range(N):
    A.append(random.randint(1, 1000))
print("Generated List: ",A)

heapSort(A)    
print("Sorted List : ",A)


#program for running time analysis
x=[]
y=[]
p=int(input("Enter the number of different data set for analyzing run time : "))
print("Now program will check for",p,"datasets which have 0 to",p,"numbers of element correspondingly")
for i in range(p):
    start = timeit.default_timer()
    x.append(i)
    B=[0] * (i)
    for j in range(i):
        B[j]= random.randint(0, 1000)
    heapSort(B)
    stop = timeit.default_timer()
    y.append(stop-start)
    
plt.plot(x, y,'ob')
plt.xlabel("Number of elements in  list")
plt.ylabel("Running Time")
