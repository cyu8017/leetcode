# LeetCode 3877 - Minimum Removals To Achieve Target Xor
# https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

from typing import List


class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        mx = 0
        for x in nums:
            mx = max(mx, x)
        m = 0
        if mx > 0:
            u = mx
            while u != 0:
                m += 1
                u >>= 1
        if (1 << m) <= target:
            return -1
        n = len(nums)
        N = 1 << m
        NEG = float("-inf")
        f = [[NEG] * N for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            x = nums[i - 1]
            for j in range(N):
                f[i][j] = f[i - 1][j]
                if f[i - 1][j ^ x] != NEG:
                    f[i][j] = max(f[i][j], f[i - 1][j ^ x] + 1)
        if f[n][target] < 0:
            return -1
        return n - int(f[n][target])
