# LeetCode 2078 - Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i, c in enumerate(colors):
            if c != colors[0]:
                ans = max(ans, i)
            if c != colors[n - 1]:
                ans = max(ans, n - 1 - i)
        return ans
