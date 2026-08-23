// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

using System.Collections.Generic;

public class Solution {
    public int MaxDistance(int[][] grid) {
        int n = grid.Length;
        var q = new Queue<(int r, int c)>();
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 1) q.Enqueue((r, c));
        if (q.Count == 0 || q.Count == n * n) return -1;
        int dist = -1;
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (q.Count > 0) {
            dist++;
            int sz = q.Count;
            for (int i = 0; i < sz; i++) {
                var (r, c) = q.Dequeue();
                foreach (var d in dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1;
                        q.Enqueue((nr, nc));
                    }
                }
            }
        }
        return dist;
    }
}
