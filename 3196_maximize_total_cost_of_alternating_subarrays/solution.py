# LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
# https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        NEG = -10**18
        n = len(nums)
        memo = [[NEG, NEG] for _ in range(n)]

        def dfs(i: int, j: int) -> int:
            if i >= n:
                return 0
            if memo[i][j] != NEG:
                return memo[i][j]
            res = nums[i] + dfs(i + 1, 1)
            if j > 0:
                res = max(res, -nums[i] + dfs(i + 1, 0))
            memo[i][j] = res
            return res

        return dfs(0, 0)
