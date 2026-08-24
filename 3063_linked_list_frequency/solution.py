# LeetCode 3063 - Linked List Frequency
# https://leetcode.com/problems/linked-list-frequency/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = {}
        while head is not None:
            cnt[head.val] = cnt.get(head.val, 0) + 1
            head = head.next
        dummy = ListNode(0)
        for val in cnt.values():
            dummy.next = ListNode(val, dummy.next)
        return dummy.next
