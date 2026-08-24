# LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
# https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, cur = head, head.next
        while cur:
            if cur.val < 0:
                prev.next = cur.next
                cur.next = head
                head = cur
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head
