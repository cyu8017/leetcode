// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

using System;
using System.Collections.Generic;

public class Solution {
    public int SwimInWater(int[][] grid) {
        int n = grid.Length;
        var heap = new PriorityQueue<(int time, int r, int c), int>();
        bool[,] seen = new bool[n, n];
        heap.Enqueue((grid[0][0], 0, 0), grid[0][0]);
        seen[0, 0] = true;
        int[][] dirs = { new[] { -1, 0 }, new[] { 1, 0 }, new[] { 0, -1 }, new[] { 0, 1 } };
        while (heap.Count > 0) {
            var (time, r, c) = heap.Dequeue();
            if (r == n - 1 && c == n - 1) return time;
            foreach (var d in dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !seen[nr, nc]) {
                    seen[nr, nc] = true;
                    int nt = Math.Max(time, grid[nr][nc]);
                    heap.Enqueue((nt, nr, nc), nt);
                }
            }
        }
        return -1;
    }
}
