# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 18:17:57 2014

@author: Mark
"""

from data_structures import BinarySearchTree, Queue, LinkedList

# initialise the BST

B = BinarySearchTree()
for k in [7,3,11,1,5,9,13,0,2,4,6,8,10,12,14]:
    B.insert(k)
    
# breadth first search
Q = Queue()

Q.enqueue(B.root)

while Q.length() > 0:
    node = Q.dequeue()
    Q.enqueue(node.left)
    Q.enqueue(node.right)
    print node.data
    
