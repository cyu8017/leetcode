# LeetCode 2848 - Points That Intersect With Cars
# https://leetcode.com/problems/points-that-intersect-with-cars/

from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cov = [0] * 102
        for a, b in nums:
            for x in range(a, b + 1):
                cov[x] = 1
        return sum(cov)
