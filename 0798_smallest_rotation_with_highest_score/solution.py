# LeetCode 0798 - Smallest Rotation with Highest Score
# https://leetcode.com/problems/smallest-rotation-with-highest-score/

from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        change = [1] * n
        for i, value in enumerate(nums):
            change[(i - value + 1) % n] -= 1
        for i in range(1, n):
            change[i] += change[i - 1]
        return change.index(max(change))
