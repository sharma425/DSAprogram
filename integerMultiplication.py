# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:33:43 2021

@author: Keshav
"""
import timeit
import random
import matplotlib.pyplot as plt
import math
def integerMultiplication(N1,N2):
    n=max(len(str(N1)),len(str(N2)))
    if n==1:
        return N1*N2
    else:
        a=0
        b=0
        c=0
        d=0
        for i in range(math.floor(n/2)):
            b=b+(N1%10)*(10**i)
            N1=int(N1/10)
        for i in range(math.ceil(n/2)):
            a= a+ (N1 % 10)*(10**i)
            N1 = int(N1/10)
        for i in range(math.floor(n/2)):
            d= d+(N2 % 10)*(10 ** i)
            N2= int(N2/10)
        for i in range(math.ceil(n/2)):
            c= c+(N2%10)*(10**i)
            N2= int(N2/10)
        X=integerMultiplication(a,c)
        Y=integerMultiplication(b,d)
        Z=integerMultiplication((a+b),(c+d))
        if n%2==1:
            n=n-1
        m= X*(10**n)+(Z-X-Y)*(10**math.ceil(n/2))+Y
        return m
    
    

    
print("Enter two integer numbers for multiplication :  ")
n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
result = integerMultiplication(n1,n2)
print(result)



#program for running time analysis
x=[]
y=[]
p=int(input("Enter the number of pairs for analyzing run time : "))
print("Now program will check for",p,"pairs having digits 1 to",p+1,"correspondingly")
for i in range(p):
    start = timeit.default_timer()
    x.append(i)
    n1 = random.randint(10**i, 10**(i+1)-1)
    n2 = random.randint(10**i, 10**(i+1)-1)
    integerMultiplication(n1,n2)
    stop = timeit.default_timer()
    y.append(stop-start)
    
plt.plot(x, y,'ob')
plt.xlabel("Number of digits in each number")
plt.ylabel("Running Time")