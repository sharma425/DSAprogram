# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 09:53:19 2021

@author: Keshav
"""
import random
def minHeapify(a,i,n):
    l= i*2+1        #left
    r=i*2+2         #right
    sm = i          #small
    if l<=n and a[l]<a[sm]:
        sm =l
    if r <=n and a[r]<a[sm]:
        sm = r
    if sm !=i :
        a[sm],a[i] = a[i],a[sm]
        minHeapify(a, sm, n)
        
def buildMinHeap(l):        #function for build min heap
    n=len(l)
    for i in range(n//2,-1,-1):
        minHeapify(l, i, len(l)-1)

#function to merge
def merge(arr):
    l=[]
    for i in A:
        for j in i : 
            l.append(j)
    buildMinHeap(l)
    for i in range(len(l)-1,-1,-1):
        minHeapify(l, 0, i)
        l[0],l[i] = l[i],l[0]
    return l

n=int(input("Enter the number of list : "))
A=[]                    #list to store the lists

for i in range(n):
    k=int(input('Enter the number of elements in %d : ' %(i+1)))
    B=[]                            #list to store random elements 
    for j in range(k):
        B.append(random.randint(1, 10000))
    A.append(B)                     #list B appended in ist A
    print('randomly generated list %d is :' %(i+1),B)
print('After Sorting',merge(A))