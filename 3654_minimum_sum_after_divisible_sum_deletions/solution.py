# LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
# https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + nums[i]) % k
        inf = 10**18
        dp = [0] * (n + 1)
        best = [inf] * k
        best[0] = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + nums[i - 1]
            if best[prefix[i]] < dp[i]:
                dp[i] = best[prefix[i]]
            if dp[i] < best[prefix[i]]:
                best[prefix[i]] = dp[i]
        return dp[n]
