# LeetCode 2181 - Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        sum = 0
        p = head.next
        while p is not None:
            if p.val == 0:
                cur.next = ListNode(sum)
                cur = cur.next
                sum = 0
            else:
                sum += p.val
            p = p.next
        return dummy.next
