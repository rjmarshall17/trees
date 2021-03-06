#!/usr/bin/env python3
from pprint import pprint


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        ret = str(self.value)
        ret += " left: " + str(self.left.value) if self.left is not None else " None"
        ret += " right: " + str(self.right.value) if self.right is not None else " None"
        return ret


TREES = [
            {
              "tree": {
                "nodes": [
                  {"id": "1", "left": "2", "right": "3", "value": 1},
                  {"id": "2", "left": "4", "right": "5", "value": 2},
                  {"id": "3", "left": "6", "right": "7", "value": 3},
                  {"id": "4", "left": "8", "right": "9", "value": 4},
                  {"id": "5", "left": None, "right": None, "value": 5},
                  {"id": "6", "left": None, "right": None, "value": 6},
                  {"id": "7", "left": None, "right": None, "value": 7},
                  {"id": "8", "left": None, "right": None, "value": 8},
                  {"id": "9", "left": None, "right": None, "value": 9}
                ],
                "root": "1"
              }
            }
    ]


def nodeDepths(root):
    sum_of_depths = 0
    print("root is of type: %s" % type(root))
    stack = [(0, root)]
    while len(stack) > 0:
        depth, node = stack.pop()
        if node is None:
            continue
        sum_of_depths += depth
        if 'left' in node:
            stack.append((depth + 1, node['left']))
        if 'right' in node:
            stack.append((depth + 1, node['right']))
    return sum_of_depths


def buildTree(tree):
    tree_nodes = {}
    for node in tree['nodes']:
        tree_nodes[node['id']] = BinaryTree(node['value'])
        if node['left'] is not None:
            tree_nodes[node['id']].left = BinaryTree(node['left'])
        if node['right'] is not None:
            tree_nodes[node['id']].right = BinaryTree(node['right'])
        print(tree_nodes[node['id']])
    return tree_nodes, tree['root']


if __name__ == '__main__':
    for tree in TREES:
        the_tree, root = buildTree(tree['tree'])
        result = nodeDepths(the_tree)
        print("The result is: %d" % result)
