# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:32:07 2021

@author: Keshav
"""
import timeit
import random
import matplotlib.pyplot as plt
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(A, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and A[i] < A[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and A[largest] < A[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		A[i],A[largest] = A[largest],A[i] # swap

		# Heapify the root.
		heapify(A, n, largest)

# The main function to sort an Aay of given size
def heapSort(A):
	n = len(A)

	# Build a maxheap.
	# Since last parent will be at ((n//2)-1) we can start at that location.
	for i in range(n // 2 - 1, -1, -1):
		heapify(A, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		A[i], A[0] = A[0], A[i] # swap
		heapify(A, i, 0)

# Driver code to test above
A = []
n = int(input("Enter the no. of elements you want to sort : "))
for i in range(n):
    A.append(int(input("Enter the element : ")))
heapSort(A)
n = len(A)
print ("Sorted Aay is")
for i in range(n):
	print ("%d" %A[i]),





#program for running time analysis
x=[]
y=[]
p=int(input("Enter the number of different data set for analyzing run time : "))
for i in range(p):
    start = timeit.default_timer()
    print(start)
    x.append(i+5)
    B=[0] * (i+5)
    for i in range(i+5):
        B[i]= random.randint(0, 99)
    print(B)
    heapSort(B)
    print(B)
    stop = timeit.default_timer()
    print(stop)
    y.append(stop-start)
    
plt.plot(x, y)
plt.xlabel("Number of elements in  list")
plt.ylabel("Running Time")

