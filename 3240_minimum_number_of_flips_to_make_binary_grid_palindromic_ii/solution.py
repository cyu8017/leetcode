# LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m // 2):
            for j in range(n // 2):
                x, y = m - i - 1, n - j - 1
                cnt1 = grid[i][j] + grid[x][j] + grid[i][y] + grid[x][y]
                ans += min(cnt1, 4 - cnt1)
        if m % 2 == 1 and n % 2 == 1:
            ans += grid[m // 2][n // 2]
        diff, ones = 0, 0
        if m % 2 == 1:
            for j in range(n // 2):
                if grid[m // 2][j] == grid[m // 2][n - j - 1]:
                    ones += grid[m // 2][j] * 2
                else:
                    diff += 1
        if n % 2 == 1:
            for i in range(m // 2):
                if grid[i][n // 2] == grid[m - i - 1][n // 2]:
                    ones += grid[i][n // 2] * 2
                else:
                    diff += 1
        if ones % 4 == 0 or diff > 0:
            ans += diff
        else:
            ans += 2
        return ans
