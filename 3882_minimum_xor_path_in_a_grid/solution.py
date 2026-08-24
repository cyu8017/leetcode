# LeetCode 3882 - Minimum XOR Path in a Grid
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/

from typing import List


class Solution:
    def minXor(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[False] * 1024 for _ in range(cols)]
        for row in range(rows):
            left = [False] * 1024
            for col in range(cols):
                nxt = [False] * 1024
                value = grid[row][col]
                if row == 0 and col == 0:
                    nxt[value] = True
                else:
                    for xorv in range(1024):
                        if dp[col][xorv] or left[xorv]:
                            nxt[xorv ^ value] = True
                dp[col] = nxt
                left = nxt
        for xorv in range(1024):
            if dp[cols - 1][xorv]:
                return xorv
        return -1
