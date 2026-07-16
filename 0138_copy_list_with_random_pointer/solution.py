# LeetCode 0138 - Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional["Node"]) -> Optional["Node"]:
        if not head:
            return None

        clones: dict[int, Node] = {}

        def clone(node: Optional[Node]) -> Optional[Node]:
            if node is None:
                return None
            key = id(node)
            if key in clones:
                return clones[key]
            copy = Node(node.val)
            clones[key] = copy
            copy.next = clone(node.next)
            copy.random = clone(node.random)
            return copy

        return clone(head)
