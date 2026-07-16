# LeetCode 0445 - Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        stack1: list[int] = []
        stack2: list[int] = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head: ListNode | None = None
        while stack1 or stack2 or carry:
            total = carry
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
            carry, digit = divmod(total, 10)
            node = ListNode(digit, head)
            head = node
        return head
