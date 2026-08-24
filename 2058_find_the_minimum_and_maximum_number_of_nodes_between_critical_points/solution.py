# LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crit = []
        prev, cur, idx = head, head.next, 1
        while cur and cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (
                cur.val < prev.val and cur.val < cur.next.val
            ):
                crit.append(idx)
            prev = cur
            cur = cur.next
            idx += 1
        if len(crit) < 2:
            return [-1, -1]
        mn = crit[1] - crit[0]
        for i in range(2, len(crit)):
            mn = min(mn, crit[i] - crit[i - 1])
        return [mn, crit[-1] - crit[0]]
