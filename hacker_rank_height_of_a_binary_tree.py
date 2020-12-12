#!/usr/bin/env python3
import os

"""
The height of a binary tree is the number of edges between the tree's root and its furthest leaf.
For example, the following binary tree is of height 2:

                 4
                / \
               /   \
              2     6
             / \   /  \
            1   3 5    7
     
Function Description

Complete the getHeight or height function in the editor. It must return the height of a binary tree as an integer.

getHeight or height has the following parameter(s):

root: a reference to the root of a binary tree.

Note -The Height of binary tree with single node is taken as zero.

Input Format

The first line contains an integer n, the number of nodes in the tree.
Next line contains n space separated integer where i-th integer denotes node[i].data.

Note: Node values are inserted into a binary search tree before a reference to the tree's root
node is passed to your function. In a binary search tree, all nodes on the left branch of a node 
are less than the node value. All values on the right branch are greater than the node value.

Constraints

1 <= node.data[i] <= 20
1 <= n <= 20

Output Format

Your function should return a single integer denoting the height of the binary tree.

Sample Input

                 3
                / \
               /   \
              2     5
             /     /  \
            1     4    6
                        \
                         7

Sample Output

3

Explanation

The longest root-to-leaf path is shown below:

                 3
                / \          <--
               /   \         <--
              2     5        <--
             /     /  \      <--
            1     4    6     <--
                        \    <--
                         7   <--

There are 4 nodes in this path that are connected by 3 edges, meaning our binary 
tree's height = 3.
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    def __height__(current_node, current_height):
        if current_node is None:
            return current_height
        left_height = __height__(current_node.left, current_height + 1)
        right_height = __height__(current_node.right, current_height + 1)
        return max(left_height, right_height)
    return __height__(root,-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    expected_output = os.environ['OUTPUT_PATH'].replace('output', 'expected_output')

    tree = BinarySearchTree()

    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    results = height(tree.root)

    fptr.write(str(results))
    fptr.write('\n')

    fptr.close()
    expected_results = open(expected_output, 'r').read().rstrip()
    # print("         Output: >>%s<< %s" % (str(results), type(results)))
    # print("Expected output: >>%s<< %s" % (str(expected_results), type(expected_results)))

    assert str(results) == str(expected_results)
    print("Tests passed for: %s" % os.environ['OUTPUT_PATH'])
