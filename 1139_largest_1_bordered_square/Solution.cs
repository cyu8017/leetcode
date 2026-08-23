// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

using System;

public class Solution {
    public int Largest1BorderedSquare(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[][] left = new int[m][];
        int[][] up = new int[m][];
        for (int r = 0; r < m; r++) {
            left[r] = new int[n];
            up[r] = new int[n];
        }
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] != 0) {
                    left[r][c] = 1 + (c > 0 ? left[r][c - 1] : 0);
                    up[r][c] = 1 + (r > 0 ? up[r - 1][c] : 0);
                }
            }
        }
        int best = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) continue;
                int limit = Math.Min(left[r][c], up[r][c]);
                for (int size = limit; size > 0; size--) {
                    if (left[r - size + 1][c] >= size && up[r][c - size + 1] >= size) {
                        best = Math.Max(best, size);
                        break;
                    }
                }
            }
        }
        return best * best;
    }
}
