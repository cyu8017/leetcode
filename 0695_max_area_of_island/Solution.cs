// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

using System;

public class Solution {
    private int Dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.Length || c < 0 || c >= grid[0].Length || grid[r][c] == 0) return 0;
        grid[r][c] = 0;
        return 1 + Dfs(grid, r + 1, c) + Dfs(grid, r - 1, c) + Dfs(grid, r, c + 1) + Dfs(grid, r, c - 1);
    }

    public int MaxAreaOfIsland(int[][] grid) {
        int best = 0;
        for (int i = 0; i < grid.Length; i++)
            for (int j = 0; j < grid[0].Length; j++)
                best = Math.Max(best, Dfs(grid, i, j));
        return best;
    }
}
