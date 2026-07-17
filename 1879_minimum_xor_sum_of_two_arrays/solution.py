# LeetCode 1879 - Minimum XOR Sum of Two Arrays
# https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [float("inf")] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            i = mask.bit_count()
            if i >= n:
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                next_mask = mask | (1 << j)
                cost = dp[mask] + (nums1[i] ^ nums2[j])
                if cost < dp[next_mask]:
                    dp[next_mask] = cost

        return dp[(1 << n) - 1]
