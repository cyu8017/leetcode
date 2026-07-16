# LeetCode 1506

from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        value = 0
        nodes = {}
        for node in tree:
            nodes[node.val] = node
            value ^= node.val
            for child in node.children:
                value ^= child.val
        return nodes[value]
