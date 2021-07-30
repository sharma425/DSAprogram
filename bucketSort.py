# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:13:23 2021

@author: Keshav
"""

import random
import timeit
import matplotlib.pyplot as plt

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

N = int(input("Enter the number of elements greater then 9 for sorting: "))
A=[random.uniform(0, 1) for i in range(N)]

print("Generated List: ",A)

print("Sorted Array in descending order is")
print(bucketSort(A))



#program for running time analysis
x=[]
y=[]
p=int(input("Enter the number of different data set for analyzing run time : "))
print("Now program will check for",p,"datasets which have 10 to",p+10,"numbers of element correspondingly")
for i in range(p):
    start = timeit.default_timer()
    x.append(i+10)
    B=[0] * (i+10)
    #generating lists have elements from 10 to p+10
    B=[random.uniform(0, 1) for j in range(i+10)]

    bucketSort(B)
    stop = timeit.default_timer()
    y.append(stop-start)
    
plt.plot(x, y,'ob')
plt.xlabel("Number of elements in  list")
plt.ylabel("Running Time")

