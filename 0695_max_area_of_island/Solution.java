// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

class Solution {
    private int dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == 0) return 0;
        grid[r][c] = 0;
        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1);
    }

    public int maxAreaOfIsland(int[][] grid) {
        int best = 0;
        for (int i = 0; i < grid.length; i++)
            for (int j = 0; j < grid[0].length; j++)
                best = Math.max(best, dfs(grid, i, j));
        return best;
    }
}
