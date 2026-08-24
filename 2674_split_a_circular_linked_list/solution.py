# LeetCode 2674 - Split a Circular Linked List
# https://leetcode.com/problems/split-a-circular-linked-list/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:
        if not list:
            return [None, None]
        slow = list
        fast = list
        while fast.next is not list and fast.next.next is not list:
            slow = slow.next
            fast = fast.next.next
        if fast.next.next is list:
            fast = fast.next
        head2 = slow.next
        slow.next = list
        fast.next = head2
        return [list, head2]
