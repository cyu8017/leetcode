# LeetCode 0810 - Chalkboard XOR Game
# https://leetcode.com/problems/chalkboard-xor-game/

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return reduce(xor, nums, 0) == 0 or len(nums) % 2 == 0
