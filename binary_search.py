#!/usr/bin/env python
import math

def binary_search(A,n,T):
#A = array
#n = number of elements in array
#T = target value
#m = position of middle element
	L = 0
	R = n-1
	while L <= R:
		m = math.floor((L+R)/2)
		if A[m] < T:
			L = m + 1
		elif A[m] > T:
			R = m - 1
		else:
			return "Index of value is " + str(m)
	return "Value not found"


alist = []
for i in range(0,51):
	alist.append(2*i)

A = alist
n = len(alist)
T = int(input("Enter a number between 0 and 100:"))

print(binary_search(A,n,T))



