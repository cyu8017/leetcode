# LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
# https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

from typing import List


class Solution:
    def minEliminationTime(self, timeReq: List[int], splitTime: int) -> int:
        pq = sorted(timeReq)
        while len(pq) > 1:
            pq.pop(0)
            x = pq.pop(0)
            v = x + splitTime
            lo, hi = 0, len(pq)
            while lo < hi:
                mid = (lo + hi) >> 1
                if pq[mid] < v:
                    lo = mid + 1
                else:
                    hi = mid
            pq.insert(lo, v)
        return pq[0]
