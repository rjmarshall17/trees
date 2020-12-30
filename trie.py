#!/usr/bin/env python3

WORD_TERMINATOR = '*'


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {'count':0}
            current_node = current_node[letter]
            current_node['count'] += 1
        current_node[WORD_TERMINATOR] = True

    def search(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        if WORD_TERMINATOR not in current_node:
            return False
        return True

    def find_prefix(self, prefix):
        current_node = self.root
        for letter in prefix:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return True

    def partial(self, partial):
        current_node = self.root
        for letter in partial:
            if letter not in current_node:
                return 0
            current_node = current_node[letter]
        return current_node['count']


if __name__ == '__main__':
    trie = Trie()
    trie.add('hello')
    trie.add('apple')
    trie.add('application')
    trie.add('testing')
    trie.add('test')
    assert trie.search('test') is True
    assert trie.search('hello') is True
    assert trie.search('hi') is False
    assert trie.search('app') is False
    assert trie.find_prefix('app') is True
    print("All tests passed")