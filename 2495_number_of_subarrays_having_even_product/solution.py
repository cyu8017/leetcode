# LeetCode 2495 - Number of Subarrays Having Even Product
# https://leetcode.com/problems/number-of-subarrays-having-even-product/

from typing import List


class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        odd_len = 0
        odd = 0
        for x in nums:
            if x % 2 == 1:
                odd += 1
                odd_len += odd
            else:
                odd = 0
        return total - odd_len
