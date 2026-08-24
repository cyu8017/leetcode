# LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        s = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j]
                if s[i + 1][j + 1] <= k:
                    ans += 1
        return ans
