# LeetCode 3996 - Even Number of Knight Moves
# https://leetcode.com/problems/even-number-of-knight-moves/

from typing import List


class Solution:
    def canReach(self, start: List[int], target: List[int]) -> bool:
        return ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2)
