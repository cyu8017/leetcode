// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

using System;

public class Solution {
    public int FindMaxFish(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int Dfs(int r, int c) {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return 0;
            int fish = grid[r][c];
            grid[r][c] = 0;
            return fish + Dfs(r + 1, c) + Dfs(r - 1, c) + Dfs(r, c + 1) + Dfs(r, c - 1);
        }
        int best = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] > 0) best = Math.Max(best, Dfs(i, j));
        return best;
    }
}
