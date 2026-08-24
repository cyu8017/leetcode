# LeetCode 3217 - Delete Nodes From Linked List Present in Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next is not None:
            if pre.next.val in s:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next
