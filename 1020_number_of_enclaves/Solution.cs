// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

public class Solution {
    public int NumEnclaves(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        for (int i = 0; i < m; i++) {
            Dfs(grid, i, 0);
            Dfs(grid, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            Dfs(grid, 0, j);
            Dfs(grid, m - 1, j);
        }
        int ans = 0;
        foreach (var row in grid)
            foreach (int x in row) ans += x;
        return ans;
    }

    private void Dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.Length || c < 0 || c >= grid[0].Length || grid[r][c] != 1) return;
        grid[r][c] = 0;
        Dfs(grid, r + 1, c);
        Dfs(grid, r - 1, c);
        Dfs(grid, r, c + 1);
        Dfs(grid, r, c - 1);
    }
}
