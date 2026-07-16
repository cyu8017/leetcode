# LeetCode 0061 - Rotate List
# https://leetcode.com/problems/rotate-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        tail.next = head
        k %= length
        if k == 0:
            tail.next = None
            return head

        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
