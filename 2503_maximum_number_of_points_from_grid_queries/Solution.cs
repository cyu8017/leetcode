// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] MaxPoints(int[][] grid, int[] queries) {
        int m = grid.Length, n = grid[0].Length;
        int[] order = new int[queries.Length];
        for (int i = 0; i < order.Length; i++) order[i] = i;
        Array.Sort(order, (a, b) => queries[a].CompareTo(queries[b]));
        int[] ans = new int[queries.Length];
        bool[][] visited = new bool[m][];
        for (int i = 0; i < m; i++) visited[i] = new bool[n];
        var pq = new PriorityQueue<(int v, int r, int c), int>();
        pq.Enqueue((grid[0][0], 0, 0), grid[0][0]);
        visited[0][0] = true;
        int points = 0;
        int[][] dirs = new int[][] {
            new int[] {1, 0}, new int[] {-1, 0}, new int[] {0, 1}, new int[] {0, -1}
        };
        foreach (int qi in order) {
            int q = queries[qi];
            while (pq.Count > 0 && pq.Peek().v < q) {
                var (v, r, c) = pq.Dequeue();
                points++;
                foreach (var d in dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                        visited[nr][nc] = true;
                        pq.Enqueue((grid[nr][nc], nr, nc), grid[nr][nc]);
                    }
                }
            }
            ans[qi] = points;
        }
        return ans;
    }
}
