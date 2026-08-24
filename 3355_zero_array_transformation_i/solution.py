# LeetCode 3355 - Zero Array Transformation I
# https://leetcode.com/problems/zero-array-transformation-i/

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for q in queries:
            diff[q[0]] += 1
            diff[q[1] + 1] -= 1
        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur < nums[i]:
                return False
        return True
