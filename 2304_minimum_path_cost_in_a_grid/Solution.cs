// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

using System;

public class Solution {
    public int MinPathCost(int[][] grid, int[][] moveCost) {
        int m = grid.Length, n = grid[0].Length;
        int[] dp = (int[])grid[0].Clone();
        for (int r = 0; r < m - 1; ++r) {
            int[] next = new int[n];
            Array.Fill(next, int.MaxValue / 2);
            for (int c = 0; c < n; ++c) {
                int from = grid[r][c];
                for (int nc = 0; nc < n; ++nc)
                    next[nc] = Math.Min(next[nc], dp[c] + moveCost[from][nc] + grid[r + 1][nc]);
            }
            dp = next;
        }
        int ans = dp[0];
        for (int i = 1; i < n; i++) ans = Math.Min(ans, dp[i]);
        return ans;
    }
}
