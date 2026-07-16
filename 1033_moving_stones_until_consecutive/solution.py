# LeetCode 1033 - Moving Stones Until Consecutive
# https://leetcode.com/problems/moving-stones-until-consecutive/

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        x, y, z = sorted([a, b, c])
        if z - x == 2:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2
        return [min_moves, z - x - 2]
