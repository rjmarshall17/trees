#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:40:54 2020

@author: robmarshall
"""

class MyMinHeap:
    """A heap can be represented as a "complete" tree. All the levels are full
except the last level. For a min heap, every nodes value is <= the values of
the child nodes. For a max heap, every nodes value is >= the values of its
child nodes.

A heap in Python is represented as a list. To find the children of a node
you take the index: i, and multiply it by two and add either 1, or 2, to
the value, i.e.

Child1 = 2i + 1
Child2 = 2i + 2

To find the parent of a node, you take the floor (result rounded down) of the
index minus 1 divided by 2, i.e.:
    
Parent = (i - 1)//2

The list, or tree, is not sorted but the root node is either the smallest
number, for a min heap, or the largest number, for a max heap, in the tree/
list.
"""

    def __init__(self, array):
        self.heap = array
        self.buildHeap()
    
    # Runs in O(N) time O(1) space, done in place
    def buildHeap(self):
        parentIdx = (len(self.heap) - 1) // 2
        for curIdx in range(parentIdx,-1,-1):
            self.siftDown(curIdx, len(self.heap) - 1)
    
    # Runs in O(logN)
    def siftDown(self, curIdx, endIdx):
        child1Idx = curIdx * 2 + 1
        print("endIdx=%d" % endIdx)
        while child1Idx <= endIdx:
            print("heap at top of while: %s" % self.heap)
            child2Idx = curIdx * 2 + 2 if curIdx * 2 + 2 < endIdx else -1
            # For max heap change < to >
            print("child1Idx=%d child2Idx=%d" % (child1Idx,child2Idx))
            if child2Idx != -1 and self.heap[child2Idx] < self.heap[child1Idx]:
                idxToSwap = child2Idx
            else:
                idxToSwap = child1Idx
            # For max heap change < to >
            if self.heap[idxToSwap] < self.heap[curIdx]:
                self.swap(curIdx,idxToSwap)
                curIdx = idxToSwap
                child1Idx = curIdx * 2 + 1
            else:
                break
    
    # Runs in O(logN)
    def siftUp(self, curIdx):
        parentIdx = (curIdx - 1) // 2
        # For max heap change comparison if curIdx and parentIx to >
        while curIdx > 0 and self.heap(curIdx) < self.heap(parentIdx):
            self.swap(curIdx, parentIdx)
            curIdx = parentIdx
            parentIdx = (curIdx - 1) // 2
    
    def peek(self):
        return self.heap[0]
    
    def empty(self):
        return self.heap == []
    
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)
        
    def remove(self):
        if self.heap == []:
            return None
        print("Heap at start of remove: %s" % self.heap)
        self.swap(0,len(self.heap) - 1)
        print("Heap after swap root and end: %s" % self.heap)
        ret = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1)
        print("Heap after siftDown: %s" % self.heap)
        return ret
    
    def swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]