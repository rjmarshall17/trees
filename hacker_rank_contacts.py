#!/usr/bin/env python3
import os


"""
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where name is a string denoting a contact name. This must store name as a new contact in the application.
find_partial, where partial is a string denoting a partial name to search the application for. It must count the
number of contacts starting with partial and print the count on a new line.
Given n sequential add and find operations, perform each operation in order.

Input Format

The first line contains a single integer, denoting the number of operations to perform.
Each line of the subsequent lines contains an operation in one of the two forms defined above.

Constraints

It is guaranteed that  and  contain lowercase English letters only.
The input doesn't have any duplicate  for the  operation.
Output Format

For each find partial operation, print the number of contact names starting with  on a new line.

Sample Input

4
add hack
add hackerrank
find hac
find hak
Sample Output

2
0

Explanation

We perform the following sequence of operations:

Add a contact named hack.
Add a contact named hackerrank.
Find and print the number of contact names beginning with hac. There are currently two contact
names in the application and both of them start with hac, so we print  on a new line.
Find and print the number of contact names beginning with hak. There are currently two contact
names in the application but neither of them start with hak, so we print  on a new line.
"""


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

    def find_partial(self, partial):
        current_node = self.root
        for letter in partial:
            if letter not in current_node:
                return 0
            current_node = current_node[letter]
        return current_node['count']


def contacts(queries):
    trie = Trie()
    results = []
    for query in queries:
        query_type, value = query
        if query_type == 'add':
            trie.add(value)
        elif query_type == 'find':
            results.append(str(trie.find_partial(value)).strip())
    # print("The results are: %s" % results)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    expected_output = os.environ['OUTPUT_PATH'].replace('input','expected_output')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    assert open(expected_output).read() == '\n'.join(map(str, result)) + '\n'
    # print("The correct results were: %s" % result)
    print("The test output matched: %s" % expected_output)
