# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:12:27 2021

@author: Keshav
"""
import timeit
import random
import matplotlib.pyplot as plt

def countingSort(A):
    lar = max(A)    #find largest element in list
    ln = len(A)     
    c=[0]*(lar+1)   #initialize count array with all zero
    b=[0]*ln
    
    # Store the count of each elements in count array
    for i in range(0,ln):
        c[A[i]]+=1
    # Store the cummulative count
    for i in range(1,lar+1):
        c[i]+=c[i-1]
        
    #place the elements in output array by finding original location
    for i in range(ln-1,-1,-1):
        b[c[A[i]]-1]=A[i]
        c[A[i]]-=1
    return b

A=[]
n = int(input("Enter the no. of elements you want to sort : "))
for i in range(n):
    A.append(int(input('Enter the element %d: ' %(i+1))))
    
s=countingSort(A)
print(s)

#program for running time analysis
x=[]
y=[]
p=int(input("Enter the number of different data set for analyzing run time : "))
print()
print("Now program will check for",p,"datasets which have 0 to",p,"numbers of element correspondingly")
for i in range(p):
    start = timeit.default_timer()
    x.append(i)
    B=[0] * (i)
    for j in range(i):
        B.append(random.randint(0, 99))
    countingSort(A)
    stop = timeit.default_timer()
    y.append(stop-start)
    
plt.plot(x, y,'ob')
plt.xlabel("Number of elements in  list")
plt.ylabel("Running Time")
