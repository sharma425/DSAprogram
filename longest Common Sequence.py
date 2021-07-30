# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 09:22:23 2021

@author: Keshav
"""
import random
import timeit
import string
import matplotlib.pyplot as plt

def lcs(A, B, m, n):
  
    if m == 0 or n == 0:                     #if any of string ends
       return 0
    elif A[m-1] == B[n-1]:                   #if both character are same
       return 1 + lcs(A, B, m-1, n-1)        #return one added value on left diagomnal
    else:                                   #if both characters are not same
       return max(lcs(A, B, m, n-1), lcs(A, B, m-1, n)) 
           #return the maximum value from right diagonal
  
  
# Driver program to test the above function
A=input("Enter first string : ")
B=input("Enter second string : ")
print ("Length of LCS is ", lcs(A , B, len(A), len(B)))


#program for running time analysis
x=[]
y=[]
p=int(input("Enter the number of different data set for analyzing run time : "))
print("Now program will check for",p,"datasets which strings having 1 to",p+1,"numbers of characters correspondingly")
for i in range(p):
    start = timeit.default_timer()
    x.append(i+1)
    
    #generating random strings of different length
    str1 =  ''.join(random.choices(string.ascii_uppercase,k= i+1))
    str2 =  ''.join(random.choices(string.ascii_uppercase, k = i+1))
                      
    lcs(str1, str2, len(str1), len(str2))
    stop = timeit.default_timer()
    y.append(stop-start)
    
plt.plot(x, y,'ob')
plt.xlabel("Number of characters in string")
plt.ylabel("Running Time")