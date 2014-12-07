# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 09:18:05 2014

@author: ricmark
"""

class Stack():
    
    def __init__(self):
        self.data = []
        
    def push(self,val):
        if val is not None:
            self.data.append(val)
            
    def pop(self):
        l = len(self.data)
        if l > 0:
            val = self.data[-1]
            self.data = self.data[:-1]
            return val
            
    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
       
       
class Queue():
    
    def __init__(self):
        self.data = []
        
    def enqueue(self,data):
        if data is not None:
            self.data = [data] + self.data
        
    def dequeue(self):
        if len(self.data) > 0:
            val = self.data[-1]
            self.data = self.data[:-1]
            return val
     
    def length(self):
        return len(self.data)
    
     
class LinkedListNode():
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class LinkedList():
    
    def __init__(self):
        self.head = None
        
    def end(self):
        "Traverse to the end of the linked list and return the last node"
        current = self.head
        if current is not None:       
            while current.next is not None:
                current = current.next                
        return current
    
    def append(self,data):
        if isinstance(data,LinkedListNode):
            new_node = data
        else:
            new_node = LinkedListNode(data)    
        if self.head is not None:
            end = self.end()
            end.next = new_node
        else:
            self.head = new_node

    def print_list(self):
        current = self.head
        if current is not None:
            while current.next is not None:
                print current.data
                current = current.next


class BSTNode():
    
    def __init__(self,data):
 
        self.data = data
        self.left = None
        self.right = None
                
class BinarySearchTree():

    def __init__(self):
        self.root = None
        
    @staticmethod                        
    def _insert_node(node, root):
        """Inserts a node into the tree with the root supplied. This 
        subroutine assumes that root is a BSTNode object and not None.
        """
        
        if node.data <= root.data:
            if root.left is None:
                root.left = node
            else:
                BinarySearchTree._insert_node(node, root.left)
        else:
            if root.right is None:
                root.right = node
            else:
                BinarySearchTree._insert_node(node, root.right)
  
    def insert(self, data):
        """Outer user-friendly class method wrapper for the insert_node
        static-method subroutine."""
        
        if isinstance(data,BSTNode):
            node = data
        else:
            node = BSTNode(data)
  
        if self.root is None:
            self.root = node
        else:
            BinarySearchTree._insert_node(node, self.root)
    
    @staticmethod
    def _traverse_subtree_in_order(root):
        """Print out the result of an in-order traversal of the BST."""
        if root is None:
            return
        BinarySearchTree._traverse_subtree_in_order(root.left)
        print root.data
        BinarySearchTree._traverse_subtree_in_order(root.right)
    
    @staticmethod
    def _traverse_subtree_pre_order(root):
        """Print out the result of an pre-order traversal of the BST."""
        if root is None:
            return
        print root.data
        BinarySearchTree._traverse_subtree_pre_order(root.left)
        BinarySearchTree._traverse_subtree_pre_order(root.right)
        
    @staticmethod
    def _traverse_subtree_post_order(root):
        """Print out the result of an post-order traversal of the BST."""
        if root is None:
            return
        BinarySearchTree._traverse_subtree_post_order(root.left)
        BinarySearchTree._traverse_subtree_post_order(root.right) 
        print root.data
      
    def traverse(self, method="in_order"):
        """Traverse the Binary Search Tree"""
        if self.root is None:
            return
        else:
            if method is "in_order":
                BinarySearchTree._traverse_subtree_in_order(self.root)   
            elif method is "pre_order":
                BinarySearchTree._traverse_subtree_pre_order(self.root)
            elif method is "post_order":
                BinarySearchTree._traverse_subtree_post_order(self.root)
            else:
                raise ValueError(method)

#    def locate(self, data)
            
        
B = BinarySearchTree()

import random

for k in range(0,10):
    B.insert(random.uniform(0,1))        
        
        
    
if __name__ == "__main__":
    
    S = Stack()
    Q = Queue()
    L = LinkedList()
    
    for k in range(0,10):
        S.push(2*k)
        Q.enqueue(2*k)
        L.append(2*k)
    