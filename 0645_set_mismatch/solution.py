# LeetCode 0645 - Set Mismatch
# https://leetcode.com/problems/set-mismatch/

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [0] * (n + 1)
        duplicate = missing = -1
        for value in nums:
            seen[value] += 1
        for value in range(1, n + 1):
            if seen[value] == 2:
                duplicate = value
            elif seen[value] == 0:
                missing = value
        return [duplicate, missing]
