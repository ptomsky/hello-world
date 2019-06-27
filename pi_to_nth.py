# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:44:24 2019

@author: patto
"""
import math

def pi_prec(precision):
    if(precision<=10):
        print(round(math.pi,precision))
    else:
        print("Select precision less than 11")
    
    