# LeetCode 0861 - Score After Flipping Matrix
# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in grid:
            if row[0] == 0:
                for j in range(n):
                    row[j] ^= 1
        ans = m * (1 << (n - 1))
        for j in range(1, n):
            ones = sum(grid[i][j] for i in range(m))
            ans += max(ones, m - ones) * (1 << (n - 1 - j))
        return ans
