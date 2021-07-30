# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:31:01 2021

@author: Keshav
"""
import timeit
import random
import matplotlib.pyplot as plt
     
def partition(A,l,h):
    p=A[h]          #pivot element#
    i=l-1           # index of smaller element
    
    # If current element is smaller than or
    # equal to pivot
    for j in range(l,h):
        if A[j]>=p:
            # increment index of smaller element
            i+=1
            A[i],A[j]=A[j],A[i]
            
    A[i+1],A[h]=A[h],A[i+1]
    return i+1

# Function for Quick sort
def quickSort(A,l,h):
    if l<h:
        pivot = partition(A, l, h) #for pivot
        quickSort(A, l, pivot-1)    #recursive calling 
        quickSort(A,pivot+1, h)
        
A = []
n = int(input("Enter the no. of elements you want to sort : "))
for i in range(n):
    A.append(int(input("Enter the element : ")))
quickSort(A, 0, n-1)
print("Sorted list is",A)




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
        B.append(random.randint(0, 99))
    quickSort(B, 0, i)
    stop = timeit.default_timer()
    y.append(stop-start)
    
plt.plot(x, y,'ob')
plt.xlabel("Number of elements in  list")
plt.ylabel("Running Time")

