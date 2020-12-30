#!/usr/bin/env python3

from typing import List, Any
from collections import deque

"""
Utility classes and functions for Leet Code Binary Search Trees.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        ret = str(self.val)
        ret += " left: %s" % ("None" if self.left is None else str(self.left.val))
        ret += " right: %s" % ("None" if self.right is None else str(self.right.val))
        return ret


def breadth_first_search(tree):
    levels = []
    tree_depth = get_tree_depth(tree)
    for i in range(tree_depth):
        levels.append([None] * (2 ** i))
    # print(levels)
    queue = deque()
    queue.append(tree)
    level = 0
    while level < tree_depth:
        size = len(queue)
        # print("levels[level=%d]=%s size=%d" % (level, levels[level], size))
        for i in range(size):
            current_node = queue.popleft()
            if current_node is None:
                queue.append(None)
                queue.append(None)
            else:
                queue.append(current_node.left)
                queue.append(current_node.right)
            levels[level][i] = current_node
        # print("End of level %d: %s" % (level, levels[level]))
        level += 1
    return levels


def get_tree_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    left = get_tree_depth(root.left)
    right = get_tree_depth(root.right)
    return max(left, right) + 1


# The list of values being provided could be ints, strings, None...
def build_tree(nodes: List[Any]) -> TreeNode:
    """
    To build the tree we use the following pseudocode:
    :param nodes: List of incoming nodes
    Create a queue
    Create the root node from first element of list
    Put root into queue
    for i in length of nodes starting at 1 and using step 2
        pop current node from queue
        check if next child is None
        get left child from nodes
        add left child to queue
        check if next child is None
        get right child from nodes
        add right child to queue
    :return: root
    """
    queue = deque()
    root = TreeNode(nodes[0])
    queue.append(root)

    for i in range(1,len(nodes),2):
        current_node = queue.popleft()
        if nodes[i] is not None:
            left_node = TreeNode(nodes[i])
            queue.append(left_node)
            current_node.left = left_node
        if i + 1 < len(nodes) and nodes[i+1] is not None:
            right_node = TreeNode(nodes[i+1])
            queue.append(right_node)
            current_node.right = right_node
    return root


def print_tree(tree):
    """
    For print tree, run the breadth_first_search on the tree which will return
    a list contains a list of nodes for each level. The basic idea is that the
    last level will have an initial single space and each node will be separated
    by a space. For the second to last level, the level will start with 2 spaces
    and each node will be separated by 4. From there everything will double with
    each level.

    Pseudocode:
    get the levels from breadth_first_search()
    Count down in reverse order multiplying the initial spaces and spaces between nodes
    """
    levels = breadth_first_search(tree)
    level = 0
    for i in range(len(levels) - 1, -1 , -1):
        between = ' '*(2*(2**i))
        output = ' '*(2**i)
        # print('levels[%d]=%s' % (level, levels[level]))
        for node in levels[level]:
            output += str(node.val) if node is not None else ' '
            output += between
        print(output)
        level += 1
