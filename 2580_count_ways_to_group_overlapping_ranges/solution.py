# LeetCode 2580 - Count Ways to Group Overlapping Ranges
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 1000000007
        ranges.sort(key=lambda r: r[0])
        groups = 0
        end = -1
        for r in ranges:
            if r[0] > end:
                groups += 1
                end = r[1]
            elif r[1] > end:
                end = r[1]
        ans = 1
        for _ in range(groups):
            ans = ans * 2 % MOD
        return ans
