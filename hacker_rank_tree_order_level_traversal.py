#!/usr/bin/env python3
import os

"""
Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. In level-order traversal, nodes are visited level by level from left to right. Complete the function  and print the values in a single line separated by a space.

For example:

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4
For the above tree, the level order traversal is .

Input Format

You are given a function,

void levelOrder(Node * root) {

}
Constraints

 Nodes in the tree

Output Format

Print the values in a single line separated by a space.

Sample Input

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4
Sample Output

1 2 5 3 6 4

Explanation

We need to print the nodes level by level. We process each level from left to right.
Level Order Traversal: 1->2->5->3->6->4
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
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

def levelOrder(root):
    level_queue = [root]
    levels_traversed = 0
    results = []
    while len(level_queue) > 0:
        levels_traversed += 1
        # Time complexity is: O(N-K) where K is the index to be popped
        current_node = level_queue.pop(0)
        if isinstance(current_node.info, list):
            results.append(str(current_node.info[0]))
        else:
            results.append(str(current_node.info))
        if current_node.left is not None:
            level_queue.append(current_node.left)
        if current_node.right is not None:
            level_queue.append(current_node.right)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    expected_output = os.environ['OUTPUT_PATH'].replace('output', 'expected_output')

    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    results = levelOrder(tree.root)

    fptr.write(' '.join(map(str, results)))
    fptr.write('\n')

    fptr.close()
    # print("         Output: >>%s<<" % ' '.join(map(str, results)))
    # print("Expected output: >>%s<<" % open(expected_output, 'r').read().rstrip())

    assert ' '.join(map(str, results)) == open(expected_output, 'r').read().rstrip()
    print("Tests passed for: %s" % os.environ['OUTPUT_PATH'])
