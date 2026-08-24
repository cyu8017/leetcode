# LeetCode 2130 - Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow is not None:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        ans = 0
        a = head
        b = prev
        while b is not None:
            ans = max(ans, a.val + b.val)
            a = a.next
            b = b.next
        return ans
