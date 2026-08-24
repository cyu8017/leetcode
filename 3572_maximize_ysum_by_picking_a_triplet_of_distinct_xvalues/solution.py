# LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
# https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        arr = [[x[i], y[i]] for i in range(n)]
        arr.sort(key=lambda p: -p[1])
        ans = 0
        vis = set()
        for a, b in arr:
            if a not in vis:
                vis.add(a)
                ans += b
                if len(vis) == 3:
                    return ans
        return -1
