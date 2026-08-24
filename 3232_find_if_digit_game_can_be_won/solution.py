# LeetCode 3232 - Find if Digit Game Can Be Won
# https://leetcode.com/problems/find-if-digit-game-can-be-won/

from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a = b = 0
        for x in nums:
            if x < 10:
                a += x
            else:
                b += x
        return a != b
