#!/usr/bin/env python3

import os
import sys
from collections import deque

sys.setrecursionlimit(10000)

"""
A binary tree is a tree which is characterized by one of the following properties:

o It can be empty (null).
o It contains a root node only.
o It contains a root node with a left subtree, a right subtree, or both. These subtrees are also binary trees.

In-order traversal is performed as

1. Traverse the left subtree.
2. Visit root.
3. Traverse the right subtree.

For this in-order traversal, start from the left child of the root node and keep exploring the left subtree
until you reach a leaf. When you reach a leaf, back up to its parent, check for a right child and visit it
if there is one. If there is not a child, you've explored its left and right subtrees fully. If there is a
right child, traverse its left subtree then its right in the same manner. Keep doing this until you have
traversed the entire tree. You will only store the values of a node as you visit when one of the following 
is true:

o it is the first node visited, the first time visited
o it is a leaf, should only be visited once
o all of its subtrees have been explored, should only be visited once while this is true
o it is the root of the tree, the first time visited

Swapping: Swapping subtrees of a node means that if initially node has left subtree L and right subtree R, 
then after swapping, the left subtree will be R and the right subtree, L.

For example, in the following tree, we swap children of node 1.

                                Depth
    1               1            [1]
   / \             / \
  2   3     ->    3   2          [2]
   \   \           \   \
    4   5           5   4        [3]

In-order traversal of left tree is 2 4 1 3 5 and of right tree is 3 5 1 2 4.

Swap operation:

We define depth of a node as follows:

o The root node is at depth 1.
o If the depth of the parent node is d, then the depth of current node will be d+1.

Given a tree and an integer, k, in one operation, we need to swap the subtrees of all the nodes at each depth h,
where h ∈ [k, 2k, 3k,...]. In other words, if h is a multiple of k, swap the left and right subtrees of that level.

You are given a tree of n nodes where nodes are indexed from [1..n] and it is rooted at 1. You have to perform t 
swap operations on it, and after each swap operation print the in-order traversal of the current state of the tree.

Function Description

Complete the swapNodes function in the editor below. It should return a two-dimensional array where each element 
is an array of integers representing the node indices of an in-order traversal after a swap operation.

swapNodes has the following parameter(s):
- indexes: an array of integers representing index values of each , beginning with , the first element, as the root.
- queries: an array of integers, each representing a  value.

Input Format

The first line contains n, number of nodes in the tree.

Each of the next n lines contains two integers, a b, where a is the index of left child, and b is the index of 
right child of ith node.

Note: -1 is used to represent a null node.

The next line contains an integer, t, the size of queries.
Each of the next t lines contains an integer queries[i], each being a value k.

Output Format

For each k, perform the swap operation and store the indices of your in-order traversal to your result array.
After all swap operations have been performed, return your result array for printing.

Constraints

o 1 <= n <= 1024
o 1 <= t <= 100
o 1 <= k <= n
o Either a == -1 or 2 <= a <= n 
o Either b == -1 or 2 <= b <= n 
o The index of a non-null child will always be greater than that of its parent.

Sample Input 0

3
2 3
-1 -1
-1 -1
2
1
1

Sample Output 0

3 1 2
2 1 3

Explanation 0

As nodes 2 and 3 have no children, swapping will not have any effect on them. We only have to swap the child nodes of the root node.

    1   [s]       1    [s]       1   
   / \      ->   / \        ->  / \  
  2   3 [s]     3   2  [s]     2   3

Note: [s] indicates that a swap operation is done at this depth.

Sample Input 1

5
2 3
-1 4
-1 5
-1 -1
-1 -1
1
2

Sample Output 1

4 2 1 5 3

Explanation 1

Swapping child nodes of node 2 and 3 we get

    1                  1  
   / \                / \ 
  2   3   [s]  ->    2   3
   \   \            /   / 
    4   5          4   5  
Sample Input 2

11
2 3
4 -1
5 -1
6 -1
7 8
-1 9
-1 -1
10 11
-1 -1
-1 -1
-1 -1
2
2
4

Sample Output 2

2 9 6 4 1 3 7 5 11 8 10
2 6 9 4 1 3 7 5 10 8 11

Explanation 2

Here we perform swap operations at the nodes whose depth is either 2 or 4 for  and then at nodes whose depth is 4 for .

         1                     1                          1             
        / \                   / \                        / \            
       /   \                 /   \                      /   \           
      2     3    [s]        2     3                    2     3          
     /      /                \     \                    \     \         
    /      /                  \     \                    \     \        
   4      5          ->        4     5          ->        4     5       
  /      / \                  /     / \                  /     / \      
 /      /   \                /     /   \                /     /   \     
6      7     8   [s]        6     7     8   [s]        6     7     8
 \          / \            /           / \              \         / \   
  \        /   \          /           /   \              \       /   \  
   9      10   11        9           11   10              9     10   11 
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        ret = str(self.value) + " level: " + str(self.level)
        ret += " left: " + (str(self.left.value) if self.left is not None else "None")
        ret += " right: " + (str(self.right.value) if self.right is not None else "None")
        return ret


# def inOrder(root):
#     # Set current to root of binary tree
#     current = root
#     stack = []  # initialize stack
#     while True:
#         # print("inOrder: Start of while loop, current: %s" % current)
#         # print("inOrder: Start of while loop the stack (length: %d) is: %s" % (len(stack), ",".join([str(x) for x in stack])))
#         # Reach the left most Node of the current Node
#         if current is not None:
#             # Place pointer to a tree node on the stack
#             # before traversing the node's left subtree
#             stack.append(current)
#             print("inOrder: Current appended to stack: %s" % current)
#             current = current.left
#
#             # BackTrack from the empty subtree and visit the Node
#         # at the top of the stack; however, if the stack is
#         # empty you are done
#         elif (stack):
#             current = stack.pop()
#             print("inOrder: *** popped *** current: %s" % current)  # Python 3 printing
#
#             # We have visited the node and its left
#             # subtree. Now, it's right subtree's turn
#             current = current.right
#         # Seem to be all done, exit the while loop
#         else:
#             break


#
# The swapNodes function from the problem description.
#
def swapNodes(indexes_in, queries_in):
    root = Node(1)

    def create(root_node, indexes_to_create):
        queue = deque([root_node])
        for left, right in indexes_to_create:
            current_node = queue.popleft()

            # Create the left child, if there is one
            if left != -1:
                current_node.left = Node(left)
                queue.append(current_node.left)

            # Create the right child, if there is one
            if right != -1:
                current_node.right = Node(right)
                queue.append(current_node.right)
            # print("create: The current node is: %s" % current_node)
        return root_node

    def swap_recursive(root_to_swap, k_to_swap, level, return_list):
        if root_to_swap:
            # If we are at the correct level, swap the nodes
            if level % k_to_swap == 0:
                root_to_swap.left, root_to_swap.right = root_to_swap.right, root_to_swap.left

            # Do an in-order traversal
            swap_recursive(root_to_swap.left, k_to_swap, level + 1, return_list)
            # print("Adding value: %d" % root_to_swap.value)
            return_list.append(root_to_swap.value)
            swap_recursive(root_to_swap.right, k_to_swap, level + 1, return_list)

    # def swap_iterative(root_to_swap, k_to_swap):
    #     # print("Using iterative")
    #     print("The incoming value of k is: %d" % k)
    #     current_level = 1
    #     # print("The root to swap is: %s" % root_to_swap)
    #     swap_queue = deque([root_to_swap])
    #     return_deque = deque()
    #     return_deque.append(root_to_swap.value)
    #     while len(swap_queue) > 0:
    #         current_node = swap_queue.popleft()
    #         # print("For current_level %d current node is: %s" % (current_level, current_node))
    #         if current_node:
    #             print("swap_iterative: The current node is: %s" % current_node)
    #             print("swap_iterative: current_level (%d) %% k_to_swap (%d) = %d" % (current_level,
    #                                                                                  k_to_swap,
    #                                                                                  current_level % k_to_swap))
    #             if current_level % k_to_swap == 0:
    #                 # print("Swapping at current_level %d" % current_level)
    #                 current_node.left, current_node.right = current_node.right, current_node.left
    #                 print("swap_iterative: Post swap, current_level=%d the current node is: %s" % (current_level, current_node))
    #             if current_node.left is not None:
    #                 return_deque.appendleft(current_node.left.value)
    #             if current_node.right is not None:
    #                 return_deque.append(current_node.right.value)
    #             swap_queue.append(current_node.left)
    #             swap_queue.append(current_node.right)
    #         current_level += 1
    #     return list(return_deque)

    # def swap_iterative(root_to_swap, k_to_swap):


    # Now create the tree using the supplied indexes
    tree_root = create(root, indexes_in)
    # print("After create, the original tree is:")
    # inOrder(tree_root)
    # print("="*80)

    # Now process the queries which will swap nodes, k is the value
    # from the problem description used to denote the level for each
    # swap operation
    return_results = []
    for k in queries_in:
        recursive_swapped_values = []
        swap_recursive(tree_root, k, 1, recursive_swapped_values)
        return_results.append(recursive_swapped_values)
        # print("After swapping nodes the tree is:")
        # inOrder(tree_root)

        # return_results.append(swap_iterative(tree_root, k))

        # print("The recursive swapped values are: %s" % recursive_swapped_values)
        # print("The iterative swapped values are: %s" % iterative_swapped_values)
        # print("The current return results is: %s" % return_results)
    return return_results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

    results = '\n'.join([' '.join(map(str, x)) for x in result])
    expected_results = open(os.environ['OUTPUT_PATH'].replace('output','expected_output'), 'r').read()
    # print("The results are:\n>>%s<<" % results)
    # print("The expected results are:\n>>%s<<" % expected_results)
    assert results == expected_results
    print("The expected results:\n%s\nmatch the results:\n%s" % (expected_results, results))
