#!/usr/bin/env python3

# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None  # The nodes on the left are <
        self.right_child = None  # The nodes on the right are >


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert__(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self.__insert__(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self.__insert__(value, current_node.right_child)
        else:
            raise ValueError("Value %s is already in the tree" % value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert__(value, self.root)

    def __print_tree__(self, current_node):
        if current_node is not None:
            self.__print_tree__(current_node.left_child)
            print("%s" % current_node.value)
            self.__print_tree__(current_node.right_child)

    def print_tree(self):
        if self.root is not None:
            self.__print_tree__(self.root)

    def __height__(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self.__height__(current_node.left_child, current_height + 1)
        right_height = self.__height__(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

    def height(self):
        if self.root is not None:
            return self.__height__(self.root, 0)
        return 0

    def __search__(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child is not None:
            return self.__search__(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self.__search__(value, current_node.right_child)
        return False

    def search(self, value):
        if self.root is not None:
            ret = self.__search__(value, self.root)
            return ret
        return False


def fill_tree(tree, num_elements=100, max_int=1000):
    from random import randint
    for _ in range(num_elements):
        try:
            tree.insert(randint(0, max_int))
        except ValueError as e:
            print("%s" % e.args)
    return tree


if __name__ == '__main__':
    tree = BinarySearchTree()
    # tree = fill_tree(tree)
    # tree.print_tree()
    # print("The current height is: %d" % tree.height())
    tree.insert(0)
    tree.insert(5)
    tree.insert(6)
    tree.insert(10)
    tree.insert(20)
    tree.insert(45)
    tree.insert(15)
    tree.print_tree()
    print("Is the value %d in the tree: %s" % (5, tree.search(5)))
    print("Is the value %d in the tree: %s" % (20, tree.search(20)))
    print("Is the value %d in the tree: %s" % (99, tree.search(99)))
    print("Is the value %d in the tree: %s" % (28, tree.search(28)))
