# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:04:03 2019

@author: patto
"""

def fibonacci(length):
    fib = []
    for i in range(length):
        if i<2:
            fib.append(1)
        else:
            fib.append(fib[i-1]+fib[i-2])
    print(fib)
            
        
        
        
    