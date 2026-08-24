# LeetCode 2780 - Minimum Index of a Valid Split
# https://leetcode.com/problems/minimum-index-of-a-valid-split/

from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = {}
        dom = 0
        best = 0
        for v in nums:
            c = freq.get(v, 0) + 1
            freq[v] = c
            if c > best:
                best = c
                dom = v
        left = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == dom:
                left += 1
            right = best - left
            if left * 2 > i + 1 and right * 2 > n - i - 1:
                return i
        return -1
