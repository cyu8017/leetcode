# LeetCode 3847 - Find The Score Difference In A Game
# https://leetcode.com/problems/find-the-score-difference-in-a-game/

from typing import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        ans = 0
        k = 1
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                k = -k
            if i % 6 == 5:
                k = -k
            ans += k * nums[i]
        return ans
