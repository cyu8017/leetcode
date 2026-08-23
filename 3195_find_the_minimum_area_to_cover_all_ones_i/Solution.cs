// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

using System;

public class Solution {
    public int MinimumArea(int[][] grid) {
        int x1 = grid.Length, y1 = grid[0].Length, x2 = 0, y2 = 0;
        for (int i = 0; i < grid.Length; i++) {
            for (int j = 0; j < grid[0].Length; j++) {
                if (grid[i][j] == 1) {
                    x1 = Math.Min(x1, i); y1 = Math.Min(y1, j);
                    x2 = Math.Max(x2, i); y2 = Math.Max(y2, j);
                }
            }
        }
        return (x2 - x1 + 1) * (y2 - y1 + 1);
    }
}
