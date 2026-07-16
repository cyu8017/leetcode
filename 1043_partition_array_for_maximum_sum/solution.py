# LeetCode 1043 - Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            best = 0
            for size in range(1, min(k, i) + 1):
                best = max(best, arr[i - size])
                dp[i] = max(dp[i], dp[i - size] + best * size)
        return dp[n]
