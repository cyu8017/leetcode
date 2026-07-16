# LeetCode 0813 - Largest Sum of Averages
# https://leetcode.com/problems/largest-sum-of-averages/

from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0.0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        def average(i: int, j: int) -> float:
            return (prefix[j] - prefix[i]) / (j - i)

        dp = [average(0, i) for i in range(1, n + 1)]
        for groups in range(2, k + 1):
            nxt = [0.0] * n
            for i in range(groups - 1, n):
                best = 0.0
                for j in range(groups - 2, i):
                    best = max(best, dp[j] + average(j + 1, i + 1))
                nxt[i] = best
            dp = nxt
        return dp[-1]
