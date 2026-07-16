# LeetCode 0147 - Insertion Sort List
# https://leetcode.com/problems/insertion-sort-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = head
        while current:
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            nxt = current.next
            current.next = prev.next
            prev.next = current
            current = nxt
        return dummy.next
