# LeetCode 0228 - Summary Ranges
# https://leetcode.com/problems/summary-ranges/

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result: list[str] = []
        index = 0
        while index < len(nums):
            start = nums[index]
            while index + 1 < len(nums) and nums[index + 1] == nums[index] + 1:
                index += 1
            if start == nums[index]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[index]}")
            index += 1
        return result
