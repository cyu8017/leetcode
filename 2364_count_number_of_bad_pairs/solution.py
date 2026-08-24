# LeetCode 2364 - Count Number of Bad Pairs
# https://leetcode.com/problems/count-number-of-bad-pairs/

from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        freq = {}
        good = 0
        for i, x in enumerate(nums):
            key = x - i
            good += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1
        return total - good
