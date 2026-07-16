# LeetCode 1019 - Next Greater Node In Linked List
# https://leetcode.com/problems/next-greater-node-in-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> list[int]:
        vals: list[int] = []
        while head:
            vals.append(head.val)
            head = head.next
        ans = [0] * len(vals)
        stack: list[int] = []
        for i, x in enumerate(vals):
            while stack and vals[stack[-1]] < x:
                ans[stack.pop()] = x
            stack.append(i)
        return ans
