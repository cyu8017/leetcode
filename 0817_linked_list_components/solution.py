# LeetCode 0817 - Linked List Components
# https://leetcode.com/problems/linked-list-components/

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        present = set(nums)
        count = 0
        connected = False
        while head:
            if head.val in present:
                if not connected:
                    count += 1
                    connected = True
            else:
                connected = False
            head = head.next
        return count
