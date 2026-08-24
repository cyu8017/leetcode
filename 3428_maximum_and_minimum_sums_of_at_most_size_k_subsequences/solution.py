# LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

from typing import List


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        nums = sorted(nums)
        n = len(nums)
        C = [[0] * k for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            j = 1
            while j < k and j <= i:
                C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod
                j += 1
        ans = 0
        for i in range(n):
            ways_max = 0
            j = 0
            while j < k and j <= i:
                ways_max = (ways_max + C[i][j]) % mod
                j += 1
            ways_min = 0
            right = n - i - 1
            j = 0
            while j < k and j <= right:
                ways_min = (ways_min + C[right][j]) % mod
                j += 1
            ans = (ans + nums[i] * ways_max % mod + nums[i] * ways_min % mod) % mod
        return ans
