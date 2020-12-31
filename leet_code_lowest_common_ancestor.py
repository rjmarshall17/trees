#!/usr/bin/env python3

from typing import List


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


"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

From Wikipedia:

In graph theory and computer science, the lowest common ancestor (LCA) of two nodes v and w in 
a tree or directed acyclic graph (DAG) T is the lowest (i.e. deepest) node that has both v and
w as descendants, where we define each node to be a descendant of itself (so if v has a direct
connection from w, w is the lowest common ancestor).

According to the definition of LCA on Wikipedia: ?The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow 
a node to be a descendant of itself).?

Example 1:

                        3
                       / \
                      /   \
                     5     1
                    / \   / \
                   6   2 0   8
                      / \
                     7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

                        3
                       / \
                      /   \
                     5     1
                    / \   / \
                   6   2 0   8
                      / \
                     7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5

Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [2, 105].
-10**9 <= Node.val <= 10**9
All Node.val are unique.
p != q
p and q will exist in the tree.
"""


def print_tree(tree):
    if tree is None:
        return
    print("%s" % tree)
    print_tree(tree.left)
    print_tree(tree.right)


"""
A recursive solution for this challenge:

lowest_common_ancestor(root, p, q)
    if p < root and q < root
        lowest_common_ancestor(root.left, p, q)
    if p > root and q > root
        lowest_common_ancestor(root.right, p, q)
    return root - At this point, this should be the lowest common ancestor
"""


def lowest_common_ancestor(root, p, q):
    print("root=%s\n\tp=%s\n\tq=%s" % (root, p, q))
    if root is None:
        return None
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root


bst1_tn0 = TreeNode(0)
bst1_tn1 = TreeNode(1)
bst1_tn2 = TreeNode(2)
bst1_tn3 = TreeNode(3)
bst1_tn4 = TreeNode(4)
bst1_tn5 = TreeNode(5)
bst1_tn6 = TreeNode(6)
bst1_tn7 = TreeNode(7)
bst1_tn8 = TreeNode(8)
bst1_tn9 = TreeNode(9)

bst1_tn6.left = bst1_tn2
bst1_tn6.right = bst1_tn8
bst1_tn2.left = bst1_tn0
bst1_tn2.right = bst1_tn4
bst1_tn8.left = bst1_tn7
bst1_tn8.right = bst1_tn9
bst1_tn4.left = bst1_tn3
bst1_tn4.right = bst1_tn5

bst2_tn1 = TreeNode(1)
bst2_tn2 = TreeNode(2)
bst2_tn2.left = bst2_tn1


if __name__ == '__main__':
    print_tree(bst1_tn6)
    print('='*80)
    result = lowest_common_ancestor(bst1_tn6, bst1_tn2, bst1_tn4)
    print("The result is: %s" % result)
    print_tree(bst2_tn2)
    print('='*80)
    result = lowest_common_ancestor(bst2_tn2, bst2_tn2, bst2_tn1)
    print("The result is: %s" % result)

