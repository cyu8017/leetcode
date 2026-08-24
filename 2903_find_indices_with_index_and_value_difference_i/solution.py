# LeetCode 2903 - Find Indices With Index and Value Difference I
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if abs(j - i) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
