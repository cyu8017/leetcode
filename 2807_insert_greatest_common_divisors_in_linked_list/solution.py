# LeetCode 2807 - Insert Greatest Common Divisors in Linked List
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        cur = head
        while cur and cur.next:
            g = gcd(cur.val, cur.next.val)
            node = ListNode(g, cur.next)
            cur.next = node
            cur = node.next
        return head
