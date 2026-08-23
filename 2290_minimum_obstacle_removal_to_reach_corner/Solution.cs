// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

using System.Collections.Generic;

public class Solution {
    public int MinimumObstacles(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[,] dist = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                dist[i, j] = int.MaxValue / 2;
        dist[0, 0] = 0;
        var dq = new LinkedList<(int, int)>();
        dq.AddLast((0, 0));
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (dq.Count > 0) {
            var (r, c) = dq.First.Value; dq.RemoveFirst();
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nd = dist[r, c] + grid[nr][nc];
                if (nd < dist[nr, nc]) {
                    dist[nr, nc] = nd;
                    if (grid[nr][nc] == 0) dq.AddFirst((nr, nc));
                    else dq.AddLast((nr, nc));
                }
            }
        }
        return dist[m - 1, n - 1];
    }
}
