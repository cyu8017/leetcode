# LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
# https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

from typing import List


class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        d = [0] * n
        for i in range(1, n):
            d[i] = nums[i] - nums[i - 1]
        f = [2] * n
        g = [2] * n
        f[0] = 1
        g[n - 1] = 1
        for i in range(2, n):
            if d[i] == d[i - 1]:
                f[i] = f[i - 1] + 1
        for i in range(n - 3, -1, -1):
            if d[i + 1] == d[i + 2]:
                g[i] = g[i + 1] + 1
        ans = 3
        for i in range(n):
            ans = max(ans, max(f[i], g[i]))
            if i > 0:
                ans = max(ans, f[i - 1] + 1)
            if i + 1 < n:
                ans = max(ans, g[i + 1] + 1)
            if i > 0 and i < n - 1:
                diff = nums[i + 1] - nums[i - 1]
                if diff % 2 == 0:
                    diff = diff // 2
                    k = 3
                    if i > 1 and diff == d[i - 1]:
                        k += f[i - 1] - 1
                    if i < n - 2 and diff == d[i + 2]:
                        k += g[i + 1] - 1
                    ans = max(ans, k)
        return ans
