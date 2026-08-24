# LeetCode 2518 - Number of Great Partitions
# https://leetcode.com/problems/number-of-great-partitions/

from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        total = sum(nums)
        if total < 2 * k:
            return 0
        dp = [0] * k
        dp[0] = 1
        for x in nums:
            for s in range(k - 1, x - 1, -1):
                dp[s] = (dp[s] + dp[s - x]) % MOD
        bad = 0
        for v in dp:
            bad = (bad + v) % MOD
        all_ways = 1
        for _ in range(len(nums)):
            all_ways = all_ways * 2 % MOD
        return (all_ways - 2 * bad % MOD + MOD) % MOD
