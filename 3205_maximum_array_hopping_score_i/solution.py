# LeetCode 3205 - Maximum Array Hopping Score I
# https://leetcode.com/problems/maximum-array-hopping-score-i/

from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n

        def dfs(i: int) -> int:
            if f[i] > 0:
                return f[i]
            for j in range(i + 1, n):
                f[i] = max(f[i], (j - i) * nums[j] + dfs(j))
            return f[i]

        return dfs(0)
