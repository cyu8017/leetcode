# LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

from typing import List


class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])
        row = "".join(grid[i][j] for i in range(m) for j in range(n))
        col = "".join(grid[i][j] for j in range(n) for i in range(m))
        h_mark = [[False] * n for _ in range(m)]
        v_mark = [[False] * n for _ in range(m)]
        plen = len(pattern)
        for i in range(len(row) - plen + 1):
            if row[i : i + plen] == pattern:
                for t in range(plen):
                    pos = i + t
                    h_mark[pos // n][pos % n] = True
        for i in range(len(col) - plen + 1):
            if col[i : i + plen] == pattern:
                for t in range(plen):
                    pos = i + t
                    v_mark[pos % m][pos // m] = True
        ans = 0
        for i in range(m):
            for j in range(n):
                if h_mark[i][j] and v_mark[i][j]:
                    ans += 1
        return ans
