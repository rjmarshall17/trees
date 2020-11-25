#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:40:54 2020

@author: Rob Marshall
"""

SORTED_LIST = [8, 9, 13, 26, 29, 32, 36, 49, 58, 62, 65, 67, 69, 73, 75, 83, 85, 87, 89, 91, 92, 95, 96, 98]


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

Time complexity: for remove/get: O(1) for insert O(logN)
"""

    def __init__(self, array, min=True):
        self.heap = array[:]
        self.min = min
        self.buildHeap()

    def __repr__(self):
        return str(list(self.heap))

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return self

    def __next__(self):
        if self.empty():
            raise StopIteration
        return self.remove()

    # Runs in O(N) time O(1) space, done in place
    def buildHeap(self):
        parent_idx = (len(self.heap) - 1) // 2
        for cur_idx in range(parent_idx, -1, -1):
            if self.min:
                self.minSiftDown(cur_idx, len(self.heap) - 1)
            else:
                self.maxSiftDown(cur_idx, len(self.heap) - 1)

    # Runs in O(logN)
    def minSiftDown(self, cur_idx, end_idx):
        child1_idx = cur_idx * 2 + 1
        while child1_idx <= end_idx:
            child2_idx = cur_idx * 2 + 2 if cur_idx * 2 + 2 <= end_idx else -1
            # For max heap change < to >
            if child2_idx != -1 and self.heap[child2_idx] < self.heap[child1_idx]:
                idx2swap = child2_idx
            else:
                idx2swap = child1_idx
            # For max heap change < to >
            if self.heap[idx2swap] < self.heap[cur_idx]:
                self.swap(cur_idx, idx2swap)
                cur_idx = idx2swap
                child1_idx = cur_idx * 2 + 1
            else:
                break

    # Runs in O(logN)
    def maxSiftDown(self, cur_idx, end_idx):
        child1_idx = cur_idx * 2 + 1
        while child1_idx <= end_idx:
            child2_idx = cur_idx * 2 + 2 if cur_idx * 2 + 2 <= end_idx else -1
            # For max heap change < to >
            if child2_idx != -1 and self.heap[child2_idx] > self.heap[child1_idx]:
                idx2swap = child2_idx
            else:
                idx2swap = child1_idx
            # For max heap change < to >
            if self.heap[idx2swap] > self.heap[cur_idx]:
                self.swap(cur_idx, idx2swap)
                cur_idx = idx2swap
                child1_idx = cur_idx * 2 + 1
            else:
                break

    # Runs in O(logN)
    def minSiftUp(self, cur_idx):
        parent_idx = (cur_idx - 1) // 2
        # For max heap change comparison if cur_idx and parentIx to >
        while cur_idx > 0 and self.heap[cur_idx] < self.heap[parent_idx]:
            self.swap(cur_idx, parent_idx)
            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2

    # Runs in O(logN)
    def maxSiftUp(self, cur_idx):
        parent_idx = (cur_idx - 1) // 2
        # For max heap change comparison if cur_idx and parentIx to >
        while cur_idx > 0 and self.heap[cur_idx] > self.heap[parent_idx]:
            self.swap(cur_idx, parent_idx)
            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2
    
    def peek(self):
        return self.heap[0]
    
    def empty(self):
        return self.heap == []
    
    def insert(self, value):
        self.heap.append(value)
        if self.min:
            self.minSiftUp(len(self.heap) - 1)
        else:
            self.maxSiftUp(len(self.heap) - 1)
        
    def remove(self):
        if not self.heap:
            return None
        self.swap(0, len(self.heap) - 1)
        ret = self.heap.pop()
        if self.min:
            self.minSiftDown(0, len(self.heap) - 1)
        else:
            self.maxSiftDown(0, len(self.heap) - 1)
        return ret
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == '__main__':
    arr_in = [96, 85, 95, 92, 62, 26, 89, 87, 29, 58, 83, 75, 13, 8, 91, 9, 98, 65, 32, 69, 36, 73, 67, 49]
    print("Original list: %s" % arr_in)
    h = MyMinHeap(arr_in)
    print(" The min heap: %s" % h)
    print("Min Heap output:")
    output = []
    while not h.empty():
        output.append(h.remove())
    print(output)
    assert output == SORTED_LIST, "The min heap is incorrect"
