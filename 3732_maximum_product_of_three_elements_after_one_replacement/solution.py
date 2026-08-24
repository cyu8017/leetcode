# LeetCode 3732 - Maximum Product of Three Elements After One Replacement
# https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        n = len(a)
        A, B, C, D = a[0], a[1], a[n - 2], a[n - 1]
        x = 100000
        return max(A * B * x, C * D * x, -A * D * x)
