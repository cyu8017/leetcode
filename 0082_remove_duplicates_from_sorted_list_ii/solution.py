# LeetCode 0082 - Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                previous.next = head.next
            else:
                previous = previous.next
            head = head.next

        return dummy.next
