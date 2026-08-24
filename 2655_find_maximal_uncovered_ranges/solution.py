# LeetCode 2655 - Find Maximal Uncovered Ranges
# https://leetcode.com/problems/find-maximal-uncovered-ranges/

from typing import List


class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        ranges = sorted(ranges, key=lambda r: r[0])
        ans = []
        cur = 0
        for r in ranges:
            if r[0] > cur:
                ans.append([cur, r[0] - 1])
            if r[1] + 1 > cur:
                cur = r[1] + 1
        if cur < n:
            ans.append([cur, n - 1])
        return ans
