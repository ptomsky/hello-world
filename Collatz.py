# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 18:00:03 2019

@author: patto
"""

def Collatz(num):
    steps = 0
    while(num!=1):
        if(num%2==0):
            num = num/2
            steps = steps + 1
            if num == 1:
                break
        if(num%2!=0):
            num = (num*3)+1
            steps = steps + 1
    return steps