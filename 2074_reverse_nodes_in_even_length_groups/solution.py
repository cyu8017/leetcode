# LeetCode 2074 - Reverse Nodes in Even Length Groups
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        group = 1
        while prev.next:
            cur = prev.next
            cnt = 0
            node = cur
            while node and cnt < group:
                node = node.next
                cnt += 1
            if cnt % 2 == 0:
                rev_prev = node
                p = cur
                for _ in range(cnt):
                    nxt = p.next
                    p.next = rev_prev
                    rev_prev = p
                    p = nxt
                prev.next = rev_prev
                prev = cur
            else:
                for _ in range(cnt):
                    prev = prev.next
            group += 1
        return dummy.next
