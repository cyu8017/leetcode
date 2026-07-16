# LeetCode 0174 - Dungeon Game
# https://leetcode.com/problems/dungeon-game/

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols - 1] = dp[rows - 1][cols] = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                need = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
                dp[r][c] = 1 if need <= 0 else need
        return int(dp[0][0])
