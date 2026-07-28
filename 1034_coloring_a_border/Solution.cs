// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

using System.Collections.Generic;

public class Solution {
    public int[][] ColorBorder(int[][] grid, int row, int col, int color) {
        int m = grid.Length, n = grid[0].Length, original = grid[row][col];
        var component = new HashSet<(int, int)>();
        var stack = new Stack<(int, int)>();
        stack.Push((row, col));
        component.Add((row, col));
        int[] dr = { 1, -1, 0, 0 }, dc = { 0, 0, 1, -1 };
        while (stack.Count > 0) {
            var (r, c) = stack.Pop();
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == original && component.Add((nr, nc)))
                    stack.Push((nr, nc));
            }
        }
        var border = new List<(int, int)>();
        foreach (var (r, c) in component) {
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (!(nr >= 0 && nr < m && nc >= 0 && nc < n) || !component.Contains((nr, nc))) {
                    border.Add((r, c));
                    break;
                }
            }
        }
        foreach (var (r, c) in border) grid[r][c] = color;
        return grid;
    }
}
