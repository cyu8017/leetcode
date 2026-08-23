// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

using System.Collections.Generic;

public class Solution {
    public int MinDays(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;

        int Islands() {
            var seen = new HashSet<(int, int)>();
            int count = 0;
            for (int r = 0; r < m; r++) {
                for (int c = 0; c < n; c++) {
                    if (grid[r][c] == 1 && !seen.Contains((r, c))) {
                        count++;
                        var stack = new Stack<(int, int)>();
                        stack.Push((r, c));
                        seen.Add((r, c));
                        while (stack.Count > 0) {
                            var (x, y) = stack.Pop();
                            foreach (var (dx, dy) in new[] { (1, 0), (-1, 0), (0, 1), (0, -1) }) {
                                int nx = x + dx, ny = y + dy;
                                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1 && seen.Add((nx, ny)))
                                    stack.Push((nx, ny));
                            }
                        }
                    }
                }
            }
            return count;
        }

        if (Islands() != 1) return 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    grid[r][c] = 0;
                    if (Islands() != 1) { grid[r][c] = 1; return 1; }
                    grid[r][c] = 1;
                }
            }
        }
        return 2;
    }
}
