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
        if nodes[i+1] is not None:
            right_node = TreeNode(nodes[i+1])
            queue.append(right_node)
            current_node.right = right_node
    return root


def print_tree(tree):
    """
    For the print tree we do a level order traversal. We may want to decide how deep the
    tree goes first, however, just so that we can print it correctly.
    :param tree:
    Determine the depth of the tree
    The number of nodes per level increases as a power of 2
    Each node needs to be centered in X spaces
    The maximum width of the output will be 2**(tree depth - 1) * width of each node
    Perform a level order traversal of the tree
    create a queue
    add the tree, i.e. the first node, to the queue
    initialize the level variable
    while the queue is not empty
        pop next node from queue
        print value centered in string dependent on level
    :return: None
    """
    node_width = 5
    node_fmt = '{:^%d}' % node_width
    tree_depth = get_tree_depth(tree) - 1
    level = 0
    queue = deque()
    queue.append(tree)
    while level <= tree_depth:
        current_level = []
        for _ in range(level * tree_depth if level > 0 else 1):
            current_level.append(queue.popleft())
        filler = (' '*node_width)*(tree_depth - level)
        level += 1
        # print('current level: %s' % current_level)
        print(filler,end='')
        for current_node in current_level:
            if current_node is None:
                print(' '*node_width,end='')
            else:
                print(node_fmt.format(current_node.val),end='')
            if current_node is not None:
                queue.append(current_node.left)
                queue.append(current_node.right)
        print()
            # current_node =
            # for _ in range(tree_depth - level):
            #     print('-' * node_width, end='')
            # level += 1
            # print(node_fmt.format(current_node.val if current_node != '' else ''))
            # queue.append(current_node.left if current_node.left is not None else '')
            # queue.append(current_node.right if current_node.right is not None else '')
