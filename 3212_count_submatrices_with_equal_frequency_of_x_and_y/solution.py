# LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        s = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j][0] = s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0]
                if grid[i - 1][j - 1] == "X":
                    s[i][j][0] += 1
                s[i][j][1] = s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1]
                if grid[i - 1][j - 1] == "Y":
                    s[i][j][1] += 1
                if s[i][j][0] > 0 and s[i][j][0] == s[i][j][1]:
                    ans += 1
        return ans
