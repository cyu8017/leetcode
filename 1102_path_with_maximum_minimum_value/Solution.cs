// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumMinimumPath(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        var heap = new PriorityQueue<(int r, int c), int>();
        heap.Enqueue((0, 0), -grid[0][0]);
        var seen = new bool[m, n];
        seen[0, 0] = true;
        int[] dr = { 1, -1, 0, 0 };
        int[] dc = { 0, 0, 1, -1 };
        while (heap.Count > 0) {
            heap.TryDequeue(out var pos, out int negVal);
            int val = -negVal;
            int r = pos.r, c = pos.c;
            if (r == m - 1 && c == n - 1) {
                return val;
            }
            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen[nr, nc]) {
                    seen[nr, nc] = true;
                    heap.Enqueue((nr, nc), -Math.Min(val, grid[nr][nc]));
                }
            }
        }
        return grid[0][0];
    }
}
