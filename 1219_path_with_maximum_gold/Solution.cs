// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

using System;

public class Solution {
    public int GetMaximumGold(int[][] grid) {
        int rows = grid.Length, cols = grid[0].Length;
        int ans = 0;

        int Dfs(int r, int c) {
            int gold = grid[r][c];
            grid[r][c] = 0;
            int best = 0;
            int[] dr = { 1, -1, 0, 0 };
            int[] dc = { 0, 0, 1, -1 };
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] != 0) {
                    best = Math.Max(best, Dfs(nr, nc));
                }
            }
            grid[r][c] = gold;
            return gold + best;
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != 0) ans = Math.Max(ans, Dfs(r, c));
            }
        }
        return ans;
    }
}
