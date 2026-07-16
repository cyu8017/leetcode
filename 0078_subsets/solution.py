# LeetCode 0078 - Subsets
# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = [[]]

        for num in nums:
            for i in range(len(result)):
                result.append(result[i] + [num])

        return result
