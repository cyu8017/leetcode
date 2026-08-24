# LeetCode 3062 - Winner of the Linked List Game
# https://leetcode.com/problems/winner-of-the-linked-list-game/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd = 0
        even = 0
        while head is not None:
            a = head.val
            b = head.next.val
            if a < b:
                odd += 1
            if a > b:
                even += 1
            head = head.next.next
        if odd > even:
            return "Odd"
        if odd < even:
            return "Even"
        return "Tie"
