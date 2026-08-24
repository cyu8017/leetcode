# LeetCode 3218 - Minimum Cost for Cutting Cake I
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        i = j = 0
        h = v = 1
        ans = 0
        while i < m - 1 or j < n - 1:
            if j == n - 1 or (i < m - 1 and horizontalCut[i] > verticalCut[j]):
                ans += horizontalCut[i] * v
                h += 1
                i += 1
            else:
                ans += verticalCut[j] * h
                v += 1
                j += 1
        return ans
