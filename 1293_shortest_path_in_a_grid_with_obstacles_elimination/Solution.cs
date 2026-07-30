// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

using System.Collections.Generic;

public class Solution {
    public int ShortestPath(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        if (k >= m + n - 2) return m + n - 2;
        var queue = new Queue<(int r, int c, int remaining, int distance)>();
        var best = new Dictionary<(int, int), int> { [(0, 0)] = k };
        queue.Enqueue((0, 0, k, 0));
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (queue.Count > 0) {
            var (r, c, remaining, distance) = queue.Dequeue();
            if (r == m - 1 && c == n - 1) return distance;
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int nxt = remaining - grid[nr][nc];
                if (nxt < 0) continue;
                if (best.TryGetValue((nr, nc), out int prev) && nxt <= prev) continue;
                best[(nr, nc)] = nxt;
                queue.Enqueue((nr, nc, nxt, distance + 1));
            }
        }
        return -1;
    }
}
