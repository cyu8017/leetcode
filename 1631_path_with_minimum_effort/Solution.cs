// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumEffortPath(int[][] heights) {
        int m = heights.Length, n = heights[0].Length;
        var dist = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                dist[i, j] = int.MaxValue;
        dist[0, 0] = 0;
        var pq = new PriorityQueue<(int i, int j), int>();
        pq.Enqueue((0, 0), 0);
        int[] di = { 1, -1, 0, 0 };
        int[] dj = { 0, 0, 1, -1 };
        while (pq.Count > 0) {
            pq.TryDequeue(out var cell, out int effort);
            if (cell.i == m - 1 && cell.j == n - 1) return effort;
            if (effort != dist[cell.i, cell.j]) continue;
            for (int d = 0; d < 4; d++) {
                int x = cell.i + di[d], y = cell.j + dj[d];
                if (x < 0 || x >= m || y < 0 || y >= n) continue;
                int nd = Math.Max(effort, Math.Abs(heights[cell.i][cell.j] - heights[x][y]));
                if (nd < dist[x, y]) {
                    dist[x, y] = nd;
                    pq.Enqueue((x, y), nd);
                }
            }
        }
        return 0;
    }
}
