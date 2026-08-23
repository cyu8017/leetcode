// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

public class Solution {
    public int CountUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[,] grid = new int[m, n];
        foreach (var w in walls) grid[w[0], w[1]] = 2;
        foreach (var g in guards) grid[g[0], g[1]] = 2;
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        foreach (var g in guards) {
            foreach (var d in dirs) {
                int r = g[0] + d[0], c = g[1] + d[1];
                while (r >= 0 && r < m && c >= 0 && c < n && grid[r, c] != 2) {
                    grid[r, c] = 1;
                    r += d[0]; c += d[1];
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i, j] == 0) ans++;
        return ans;
    }
}
