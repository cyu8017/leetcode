# LeetCode 2464 - Minimum Subarrays in a Valid Split
# https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

from typing import List


class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        n = len(nums)
        INF = 1 << 30
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] >= INF:
                continue
            for j in range(i, n):
                if gcd(nums[i], nums[j]) > 1:
                    if dp[i] + 1 < dp[j + 1]:
                        dp[j + 1] = dp[i] + 1
        return -1 if dp[n] >= INF else dp[n]
