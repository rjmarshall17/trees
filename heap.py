#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:40:54 2020

@author: Rob Marshall
"""

MINIMUM_HEAP_LIST = [8, 9, 13, 26, 29, 32, 36, 49, 58, 62, 65, 67, 69, 73, 75, 83, 85, 87, 89, 91, 92, 95, 96, 98]
MAXIMUM_HEAP_LIST = [98, 96, 95, 92, 91, 89, 87, 85, 83, 75, 73, 69, 67, 65, 62, 58, 49, 36, 32, 29, 26, 13, 9, 8]


class MyHeap:
    """
    A heap can be represented as a "complete" tree. All the levels are full
    except the last level. For a min heap, every nodes value is <= the values of
    the child nodes. For a max heap, every nodes value is >= the values of its
    child nodes.

    A heap in Python is represented as a list. To find the children of a node
    you take the index: i, and multiply it by two and add either 1, or 2, to
    the value, i.e.

    Child1 = 2i + 1
    Child2 = 2i + 2

    To find the parent of a node, you take the floor (integer result rounded down)
    of the child index minus 1 divided by 2, i.e.:
    
    Parent = (i - 1)//2

    The list, or tree, is not sorted but the root node is either the smallest
    number, for a min heap, or the largest number, for a max heap, in the tree/
    list.

    Time complexity: for pop/peek: O(1) for push O(logN)
    """

    def __init__(self, array, min=True):
        self.heap = array[:]
        self.min = min
        self.build_heap()

    def __repr__(self):
        return str(list(self.heap))

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return self

    def __next__(self):
        if self.empty():
            raise StopIteration
        return self.pop()

    # Runs in O(N) time O(1) space, done in place
    def build_heap(self):
        parent_idx = (len(self.heap) - 1) // 2
        for cur_idx in range(parent_idx, -1, -1):
            if self.min:
                self.minimum_sift_down(cur_idx, len(self.heap) - 1)
            else:
                self.maximum_sift_down(cur_idx, len(self.heap) - 1)

    # Runs in O(logN)
    def minimum_sift_down(self, cur_idx, end_idx):
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
                self.__swap__(cur_idx, idx2swap)
                cur_idx = idx2swap
                child1_idx = cur_idx * 2 + 1
            else:
                break

    # Runs in O(logN)
    def maximum_sift_down(self, cur_idx, end_idx):
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
                self.__swap__(cur_idx, idx2swap)
                cur_idx = idx2swap
                child1_idx = cur_idx * 2 + 1
            else:
                break

    # Runs in O(logN)
    def minimum_sift_up(self, cur_idx):
        parent_idx = (cur_idx - 1) // 2
        # For max heap change comparison if cur_idx and parentIx to >
        while cur_idx > 0 and self.heap[cur_idx] < self.heap[parent_idx]:
            self.__swap__(cur_idx, parent_idx)
            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2

    # Runs in O(logN)
    def maximum_sift_up(self, cur_idx):
        parent_idx = (cur_idx - 1) // 2
        # For max heap change comparison if cur_idx and parentIx to >
        while cur_idx > 0 and self.heap[cur_idx] > self.heap[parent_idx]:
            self.__swap__(cur_idx, parent_idx)
            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2
    
    def peek(self):
        return self.heap[0]
    
    def empty(self):
        return self.heap == []
    
    def push(self, value):
        self.heap.append(value)
        if self.min:
            self.minimum_sift_up(len(self.heap) - 1)
        else:
            self.maximum_sift_up(len(self.heap) - 1)
        
    def pop(self):
        if not self.heap:
            return None
        self.__swap__(0, len(self.heap) - 1)
        ret = self.heap.pop()
        if self.min:
            self.minimum_sift_down(0, len(self.heap) - 1)
        else:
            self.maximum_sift_down(0, len(self.heap) - 1)
        return ret
    
    def __swap__(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == '__main__':
    arr_in = [96, 85, 95, 92, 62, 26, 89, 87, 29, 58, 83, 75, 13, 8, 91, 9, 98, 65, 32, 69, 36, 73, 67, 49]
    print("Original list: %s" % arr_in)
    minimum_heap = MyHeap(arr_in[:-10])
    for item in arr_in[-10:]:
        minimum_heap.push(item)
    print(" The min heap: %s" % minimum_heap)
    print("Min Heap output:")
    output = []
    while not minimum_heap.empty():
        output.append(minimum_heap.pop())
    print(output)
    assert output == MINIMUM_HEAP_LIST, "The min heap is incorrect"
    print("="*80)
    maximum_heap = MyHeap(arr_in[:-10], min=False)
    for item in arr_in[-10:]:
        maximum_heap.push(item)
    print(" The max heap: %s" % maximum_heap)
    print("Max Heap output:")
    output = []
    while not maximum_heap.empty():
        output.append(maximum_heap.pop())
    print(output)
    assert output == MAXIMUM_HEAP_LIST, "The min heap is incorrect"
