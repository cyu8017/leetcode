// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

using System.Collections.Generic;

public class Solution {
    public int MinimumTime(int[][] grid) {
        if (grid[0][1] > 1 && grid[1][0] > 1) return -1;
        int m = grid.Length, n = grid[0].Length;
        int[][] dist = new int[m][];
        for (int i = 0; i < m; i++) {
            dist[i] = new int[n];
            for (int j = 0; j < n; j++) dist[i][j] = 1 << 30;
        }
        var h = new PriorityQueue<(int t, int r, int c), int>();
        h.Enqueue((0, 0, 0), 0);
        dist[0][0] = 0;
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (h.Count > 0) {
            var (t, r, c) = h.Dequeue();
            if (r == m - 1 && c == n - 1) return t;
            if (t > dist[r][c]) continue;
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nt = t + 1;
                if (nt < grid[nr][nc]) {
                    int wait = grid[nr][nc] - nt;
                    if (wait % 2 == 1) wait++;
                    nt += wait;
                }
                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt;
                    h.Enqueue((nt, nr, nc), nt);
                }
            }
        }
        return -1;
    }
}
