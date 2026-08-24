# LeetCode 3263 - Convert Doubly Linked List to Array I
# https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, prev: Optional["Node"] = None, next: Optional["Node"] = None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def toArray(self, head: Optional[Node]) -> List[int]:
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        return ans
