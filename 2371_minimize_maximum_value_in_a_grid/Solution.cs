// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] MinScore(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        var arr = new List<(int v, int r, int c)>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                arr.Add((grid[i][j], i, j));
        arr.Sort((a, b) => a.v.CompareTo(b.v));
        int[] rowMax = new int[m], colMax = new int[n];
        var ans = new int[m][];
        for (int i = 0; i < m; i++) ans[i] = new int[n];
        foreach (var cel in arr) {
            int val = Math.Max(rowMax[cel.r], colMax[cel.c]) + 1;
            ans[cel.r][cel.c] = val;
            rowMax[cel.r] = val;
            colMax[cel.c] = val;
        }
        return ans;
    }
}
