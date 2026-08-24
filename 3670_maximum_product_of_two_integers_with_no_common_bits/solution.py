# LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
# https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_v = max(nums) if nums else 0
        bits_n = 0
        x = max_v
        while x > 0:
            bits_n += 1
            x >>= 1
        if bits_n == 0:
            bits_n = 1
        size = 1 << bits_n
        best = [0] * size
        for v in nums:
            if v > best[v]:
                best[v] = v
        for mask in range(size):
            for b in range(bits_n):
                if mask & (1 << b):
                    sub = mask ^ (1 << b)
                    if best[sub] > best[mask]:
                        best[mask] = best[sub]
        ans = 0
        for v in nums:
            comp = (size - 1) ^ v
            if best[comp] > 0:
                p = v * best[comp]
                if p > ans:
                    ans = p
        return ans
