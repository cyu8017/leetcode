# LeetCode 2905 - Find Indices With Index and Value Difference II
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        min_idx = 0
        max_idx = 0
        for j in range(indexDifference, n):
            i = j - indexDifference
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
            if nums[j] - nums[min_idx] >= valueDifference:
                return [min_idx, j]
            if nums[max_idx] - nums[j] >= valueDifference:
                return [max_idx, j]
        return [-1, -1]
