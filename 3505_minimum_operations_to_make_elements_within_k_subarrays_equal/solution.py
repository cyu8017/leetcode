# LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        min_ops = [0] * (n - x + 1)
        for i in range(n - x + 1):
            w = sorted(nums[i : i + x])
            med = w[(x - 1) // 2]
            ops = 0
            for v in w:
                ops += abs(v - med)
            min_ops[i] = ops
        inf = 10**18
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0
        for i in range(n - 1, -1, -1):
            for j in range(k + 1):
                dp[i][j] = dp[i + 1][j]
                if j > 0 and i + x <= n and min_ops[i] + dp[i + x][j - 1] < dp[i][j]:
                    dp[i][j] = min_ops[i] + dp[i + x][j - 1]
        return dp[0][k]
