// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

import java.util.Arrays;

class Solution {
    public int minPathCost(int[][] grid, int[][] moveCost) {
        int m = grid.length, n = grid[0].length;
        int[] dp = grid[0].clone();
        for (int r = 0; r < m - 1; ++r) {
            int[] next = new int[n];
            Arrays.fill(next, Integer.MAX_VALUE / 2);
            for (int c = 0; c < n; ++c) {
                int from = grid[r][c];
                for (int nc = 0; nc < n; ++nc)
                    next[nc] = Math.min(next[nc], dp[c] + moveCost[from][nc] + grid[r + 1][nc]);
            }
            dp = next;
        }
        int ans = dp[0];
        for (int i = 1; i < n; i++) ans = Math.min(ans, dp[i]);
        return ans;
    }
}
