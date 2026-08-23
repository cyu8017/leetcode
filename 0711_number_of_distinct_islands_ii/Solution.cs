// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int NumDistinctIslands2(int[][] grid) {
        if (grid == null || grid.Length == 0) return 0;
        int m = grid.Length, n = grid[0].Length;
        var shapes = new HashSet<string>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    var cells = new List<(int, int)>();
                    Dfs(grid, i, j, m, n, cells);
                    shapes.Add(Canonical(cells));
                }
            }
        }
        return shapes.Count;
    }

    private void Dfs(int[][] grid, int r, int c, int m, int n, List<(int, int)> cells) {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) return;
        grid[r][c] = 0;
        cells.Add((r, c));
        Dfs(grid, r + 1, c, m, n, cells);
        Dfs(grid, r - 1, c, m, n, cells);
        Dfs(grid, r, c + 1, m, n, cells);
        Dfs(grid, r, c - 1, m, n, cells);
    }

    private string Canonical(List<(int x, int y)> cells) {
        Func<int, int, (int, int)>[] transforms = {
            (x, y) => (x, y), (x, y) => (x, -y), (x, y) => (-x, y), (x, y) => (-x, -y),
            (x, y) => (y, x), (x, y) => (y, -x), (x, y) => (-y, x), (x, y) => (-y, -x),
        };
        string best = null;
        foreach (var transform in transforms) {
            var pts = cells.Select(p => transform(p.x, p.y)).ToList();
            int minX = pts.Min(p => p.Item1), minY = pts.Min(p => p.Item2);
            pts = pts.Select(p => (p.Item1 - minX, p.Item2 - minY)).OrderBy(p => p.Item1).ThenBy(p => p.Item2).ToList();
            string key = string.Join(";", pts);
            if (best == null || string.CompareOrdinal(key, best) < 0) best = key;
        }
        return best;
    }
}
