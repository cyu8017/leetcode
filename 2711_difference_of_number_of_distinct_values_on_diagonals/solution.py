# LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                top, bot = set(), set()
                r, c = i - 1, j - 1
                while r >= 0 and c >= 0:
                    top.add(grid[r][c])
                    r -= 1
                    c -= 1
                r, c = i + 1, j + 1
                while r < m and c < n:
                    bot.add(grid[r][c])
                    r += 1
                    c += 1
                ans[i][j] = abs(len(top) - len(bot))
        return ans
