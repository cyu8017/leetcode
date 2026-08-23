// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

using System;

public class Solution {
    public int MaxIncreaseKeepingSkyline(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[] rowMax = new int[m], colMax = new int[n];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) {
                rowMax[r] = Math.Max(rowMax[r], grid[r][c]);
                colMax[c] = Math.Max(colMax[c], grid[r][c]);
            }
        int ans = 0;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                ans += Math.Min(rowMax[r], colMax[c]) - grid[r][c];
        return ans;
    }
}
