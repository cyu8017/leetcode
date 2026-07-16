# LeetCode 0092 - Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        before = dummy
        for _ in range(left - 1):
            before = before.next

        start = before.next
        current = start.next

        for _ in range(right - left):
            start.next = current.next
            current.next = before.next
            before.next = current
            current = start.next

        return dummy.next
