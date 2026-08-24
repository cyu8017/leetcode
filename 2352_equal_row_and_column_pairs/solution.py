# LeetCode 2352 - Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        freq = {}
        for i in range(n):
            key = tuple(grid[i])
            freq[key] = freq.get(key, 0) + 1
        ans = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            ans += freq.get(col, 0)
        return ans
