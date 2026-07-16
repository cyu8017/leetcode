# LeetCode 0565 - Array Nesting
# https://leetcode.com/problems/array-nesting/

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        best = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            length = 0
            j = i
            while nums[j] >= 0:
                nxt = nums[j]
                nums[j] = -1
                j = nxt
                length += 1
            best = max(best, length)
        return best
