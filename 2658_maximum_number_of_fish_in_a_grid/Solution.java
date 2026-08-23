// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution {
    public int findMaxFish(int[][] grid) {
        int m = grid.length, n = grid[0].length, best = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] > 0) best = Math.max(best, dfs(grid, i, j));
        return best;
    }

    private int dfs(int[][] grid, int r, int c) {
        int m = grid.length, n = grid[0].length;
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return 0;
        int fish = grid[r][c];
        grid[r][c] = 0;
        return fish + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1);
    }
}
