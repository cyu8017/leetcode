# LeetCode 0025 - Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_previous = dummy

        while True:
            kth = group_previous
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            previous = group_next
            current = group_previous.next

            while current != group_next:
                nxt = current.next
                current.next = previous
                previous = current
                current = nxt

            tmp = group_previous.next
            group_previous.next = kth
            group_previous = tmp
