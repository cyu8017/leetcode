# LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen: dict[int, ListNode] = {0: dummy}
        node = dummy
        while node:
            prefix += node.val
            seen[prefix] = node
            node = node.next
        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            node.next = seen[prefix].next
            node = node.next
        return dummy.next
