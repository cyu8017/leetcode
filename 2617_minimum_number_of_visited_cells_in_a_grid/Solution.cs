// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

using System.Collections.Generic;

public class Solution {
    public int MinimumVisitedCells(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[][] dist = new int[m][];
        for (int i = 0; i < m; i++) {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++) dist[i][j] = -1;
        }
        var q = new Queue<(int, int)>();
        q.Enqueue((0, 0));
        dist[0][0] = 1;
        while (q.Count > 0) {
            var (r, c) = q.Dequeue();
            if (r == m - 1 && c == n - 1) return dist[r][c];
            for (int nc = c + 1; nc <= c + grid[r][c] && nc < n; ++nc) {
                if (dist[r][nc] == -1) {
                    dist[r][nc] = dist[r][c] + 1;
                    q.Enqueue((r, nc));
                }
            }
            for (int nr = r + 1; nr <= r + grid[r][c] && nr < m; ++nr) {
                if (dist[nr][c] == -1) {
                    dist[nr][c] = dist[r][c] + 1;
                    q.Enqueue((nr, c));
                }
            }
        }
        return -1;
    }
}
