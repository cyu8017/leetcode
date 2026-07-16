# LeetCode 0152 - Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = max_prod = min_prod = nums[0]
        for num in nums[1:]:
            candidates = (num, max_prod * num, min_prod * num)
            max_prod = max(candidates)
            min_prod = min(candidates)
            best = max(best, max_prod)
        return best
