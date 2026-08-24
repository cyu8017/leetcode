# LeetCode 2304 - Minimum Path Cost in a Grid
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]
        for r in range(m - 1):
            nxt = [2147483647 // 2] * n
            for c in range(n):
                frm = grid[r][c]
                for nc in range(n):
                    nxt[nc] = min(nxt[nc], dp[c] + moveCost[frm][nc] + grid[r + 1][nc])
            dp = nxt
        ans = dp[0]
        for i in range(1, n):
            ans = min(ans, dp[i])
        return ans
