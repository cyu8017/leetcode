# LeetCode 2786 - Visit Array Positions to Maximize Score
# https://leetcode.com/problems/visit-array-positions-to-maximize-score/

from typing import List


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        NEG = -10**18
        even = odd = nums[0]
        if nums[0] % 2 == 0:
            odd = NEG
        else:
            even = NEG
        for i in range(1, len(nums)):
            v = nums[i]
            if v % 2 == 0:
                even = max(even + v, odd + v - x)
            else:
                odd = max(odd + v, even + v - x)
        return max(even, odd)
