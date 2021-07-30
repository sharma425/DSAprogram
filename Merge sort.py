# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:32:07 2021

@author: Keshav
"""
import timeit
import random
import matplotlib.pyplot as plt


def merge(A, l, mid, r):
    n1 = mid - l + 1
    n2 = r- mid

    L = [0] * (n1)
    R = [0] * (n2)
  
    for i in range(0 , n1):
        L[i] = A[l + i]
  
    for j in range(0 , n2):
        R[j] = A[mid + 1 + j]
    i = 0    
    j = 0    
    k = l     
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < n1:       #copied remaining elements in L
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:        #copied remaining elements in R
        A[k] = R[j]
        j += 1
        k += 1
        
def mergeSort(A,l,r):               
    if l < r:               #at least two elements are there
        m = (l+(r-1))//2            #for pivot
        mergeSort(A, l, m)          #resursive calling
        mergeSort(A, m+1, r)
        merge(A, l, m, r)           #merging
  

A = []
n = int(input("Enter the no. of elements you want to sort : "))
for i in range(n):
    A.append(int(input("Enter the element : ")))
n = len(A)
mergeSort(A,0,n-1)
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
        B[j]= random.randint(0, 99)
    #print(i,"th generated list with",i,"elements is",B)
    mergeSort(B, 0, len(B)-1)
    #print(i,"th sorted list is",B)
    stop = timeit.default_timer()
    y.append(stop-start)
    
plt.plot(x, y,'ob')
plt.xlabel("Number of elements in  list")
plt.ylabel("Running Time")

