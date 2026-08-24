# LeetCode 2660 - Determine the Winner of a Bowling Game
# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(p: List[int]) -> int:
            s = 0
            for i, pins in enumerate(p):
                mul = 1
                if (i > 0 and p[i - 1] == 10) or (i > 1 and p[i - 2] == 10):
                    mul = 2
                s += mul * pins
            return s

        a, b = score(player1), score(player2)
        if a > b:
            return 1
        if b > a:
            return 2
        return 0
