# LeetCode 3294 - Convert Doubly Linked List to Array II
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def toArray(self, node: Optional[Node]) -> List[int]:
        while node is not None and node.prev is not None:
            node = node.prev
        ans = []
        while node is not None:
            ans.append(node.val)
            node = node.next
        return ans
