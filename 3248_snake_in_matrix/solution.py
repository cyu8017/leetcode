# LeetCode 3248 - Snake in Matrix
# https://leetcode.com/problems/snake-in-matrix/

from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x = y = 0
        for c in commands:
            if c[0] == "U":
                x -= 1
            elif c[0] == "D":
                x += 1
            elif c[0] == "L":
                y -= 1
            elif c[0] == "R":
                y += 1
        return x * n + y
