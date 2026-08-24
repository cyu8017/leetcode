# LeetCode 2865 - Beautiful Towers I
# https://leetcode.com/problems/beautiful-towers-i/

from typing import List


class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        for peak in range(n):
            s = heights[peak]
            mn = heights[peak]
            for i in range(peak - 1, -1, -1):
                if heights[i] < mn:
                    mn = heights[i]
                s += mn
            mn = heights[peak]
            for i in range(peak + 1, n):
                if heights[i] < mn:
                    mn = heights[i]
                s += mn
            if s > ans:
                ans = s
        return ans
