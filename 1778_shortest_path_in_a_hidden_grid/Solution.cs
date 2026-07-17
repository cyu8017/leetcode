// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

using System.Collections.Generic;

public class Solution {
    public int FindShortestPath(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int sr = 0, sc = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == -1) {
                    sr = i;
                    sc = j;
                }
            }
        }
        int[][] dirs = { new[] { -1, 0 }, new[] { 1, 0 }, new[] { 0, -1 }, new[] { 0, 1 } };
        int[,] dist = new int[m, n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dist[i, j] = -1;
            }
        }
        var queue = new Queue<(int, int)>();
        dist[sr, sc] = 0;
        queue.Enqueue((sr, sc));
        while (queue.Count > 0) {
            var (r, c) = queue.Dequeue();
            if (grid[r][c] == 2) {
                return dist[r, c];
            }
            foreach (var d in dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 0 &&
                    dist[nr, nc] < 0) {
                    dist[nr, nc] = dist[r, c] + 1;
                    queue.Enqueue((nr, nc));
                }
            }
        }
        return -1;
    }
}
