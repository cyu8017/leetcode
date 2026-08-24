# LeetCode 3082 - Find the Sum of the Power of All Subsequences
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

from typing import List


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        n = len(nums)
        f = [[0] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(k + 1):
                f[i][j] = (f[i - 1][j] * 2) % MOD
                if j >= nums[i - 1]:
                    f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % MOD
        return f[n][k]
