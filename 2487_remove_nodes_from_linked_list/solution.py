# LeetCode 2487 - Remove Nodes From Linked List
# https://leetcode.com/problems/remove-nodes-from-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        head = rev(head)
        mx = 0
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next:
            if prev.next.val >= mx:
                mx = prev.next.val
                prev = prev.next
            else:
                prev.next = prev.next.next
        return rev(dummy.next)
