# LeetCode 2816 - Double a Number Represented as a Linked List
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        head = rev(head)
        carry = 0
        cur = head
        prev = None
        while cur:
            val = cur.val * 2 + carry
            cur.val = val % 10
            carry = val // 10
            prev = cur
            cur = cur.next
        if carry > 0 and prev is not None:
            prev.next = ListNode(carry)
        return rev(head)
