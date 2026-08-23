// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

using System.Collections.Generic;

public class Solution {
    private void Dfs(int[][] grid, int r, int c, int br, int bc, List<(int, int)> path) {
        if (r < 0 || r >= grid.Length || c < 0 || c >= grid[0].Length || grid[r][c] == 0) return;
        grid[r][c] = 0;
        path.Add((r - br, c - bc));
        Dfs(grid, r + 1, c, br, bc, path);
        Dfs(grid, r - 1, c, br, bc, path);
        Dfs(grid, r, c + 1, br, bc, path);
        Dfs(grid, r, c - 1, br, bc, path);
    }

    public int NumDistinctIslands(int[][] grid) {
        if (grid == null || grid.Length == 0) return 0;
        var shapes = new HashSet<string>();
        for (int i = 0; i < grid.Length; i++) {
            for (int j = 0; j < grid[0].Length; j++) {
                if (grid[i][j] == 1) {
                    var path = new List<(int, int)>();
                    Dfs(grid, i, j, i, j, path);
                    shapes.Add(string.Join(";", path));
                }
            }
        }
        return shapes.Count;
    }
}
