// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

using System.Collections.Generic;

public class Solution {
    public int ShortestBridge(int[][] grid) {
        int n = grid.Length;
        int[][] dirs = new[] { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        void Dfs(int r, int c) {
            if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return;
            grid[r][c] = 2;
            foreach (var d in dirs) Dfs(r + d[0], c + d[1]);
        }
        bool found = false;
        for (int i = 0; i < n && !found; i++)
            for (int j = 0; j < n && !found; j++)
                if (grid[i][j] == 1) { Dfs(i, j); found = true; }
        var q = new Queue<(int r, int c, int dist)>();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 2) q.Enqueue((i, j, 0));
        while (q.Count > 0) {
            var (r, c, dist) = q.Dequeue();
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                if (grid[nr][nc] == 1) return dist;
                if (grid[nr][nc] == 0) {
                    grid[nr][nc] = 2;
                    q.Enqueue((nr, nc, dist + 1));
                }
            }
        }
        return -1;
    }
}
