# LeetCode 2974 - Minimum Number Game
# https://leetcode.com/problems/minimum-number-game/

from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        while i + 1 < len(nums):
            t = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = t
            i += 2
        return nums
