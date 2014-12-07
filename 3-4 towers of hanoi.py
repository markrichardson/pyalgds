# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 17:18:10 2014

@author: ricmark
"""
import numpy as np
import time

# 3.4 Towers of Hanoi
from data_structures import Stack

S1 = Stack()
S2 = Stack()
S3 = Stack()

N = 5

for k in reversed(range(1,N+1)):
    S1.push(k)
  
  
def print_towers():
    l1, l2, l3 = len(S1.data), len(S2.data), len(S3.data)
    max_len = N # max(l1,l2,l3)    
    a = np.empty((max_len,3))
    a[:] = None
    if l1 > 0:
        a[max_len-l1:,0] = [x for x in reversed(S1.data)]
    if l2 > 0:
        a[max_len-l2:,1] = [x for x in reversed(S2.data)]
    if l3 > 0:    
        a[max_len-l3:,2] = [x for x in reversed(S3.data)]
    print a
    print ("")
#    raw_input("")
#    time.sleep(1)
   
    
def move(n, origin, destination, buff):
    """Move A to C, using B as a Buffer"""

    # base case    
    if n == 0:
        return    
    
    move(n-1, origin, buff, destination)

    destination.push(origin.pop())
    print_towers()

    move(n-1, buff, destination, origin)
    
    
print_towers()
move(N, S1, S3, S2)