// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

using System;
using System.Collections.Generic;

public class Solution {
    // Test harness passes the revealed grid plus start/target coordinates.
    public int FindShortestPath(int[][] grid, int r1, int c1, int r2, int c2) {
        if (r1 == r2 && c1 == c2) return 0;
        int m = grid.Length, n = grid[0].Length;
        int[][] dirs = new int[][] {
            new[] { -1, 0 }, new[] { 1, 0 }, new[] { 0, -1 }, new[] { 0, 1 }
        };
        var dist = new int[m, n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                dist[i, j] = int.MaxValue;

        var heap = new PriorityQueue<(int d, int r, int c), int>();
        dist[r1, c1] = 0;
        heap.Enqueue((0, r1, c1), 0);

        while (heap.Count > 0) {
            var (d, r, c) = heap.Dequeue();
            if (r == r2 && c == c2) return d;
            if (d > dist[r, c]) continue;
            foreach (var dir in dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0) continue;
                int nd = d + grid[nr][nc];
                if (nd < dist[nr, nc]) {
                    dist[nr, nc] = nd;
                    heap.Enqueue((nd, nr, nc), nd);
                }
            }
        }
        return -1;
    }
}
