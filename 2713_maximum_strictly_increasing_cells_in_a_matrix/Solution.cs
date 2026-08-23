// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxIncreasingCells(int[][] mat) {
        int m = mat.Length, n = mat[0].Length;
        var cells = new List<(int v, int r, int c)>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                cells.Add((mat[i][j], i, j));
        cells.Sort((a, b) => a.v.CompareTo(b.v));
        int[] rowMax = new int[m], colMax = new int[n];
        int[][] dp = new int[m][];
        for (int i = 0; i < m; i++) dp[i] = new int[n];
        int ans = 0;
        for (int i = 0; i < cells.Count; ) {
            int j = i;
            while (j < cells.Count && cells[j].v == cells[i].v) j++;
            var buf = new List<(int r, int c, int val)>();
            for (int k = i; k < j; k++) {
                int r = cells[k].r, c = cells[k].c;
                int best = Math.Max(rowMax[r], colMax[c]);
                dp[r][c] = best + 1;
                ans = Math.Max(ans, dp[r][c]);
                buf.Add((r, c, dp[r][c]));
            }
            foreach (var (r, c, val) in buf) {
                rowMax[r] = Math.Max(rowMax[r], val);
                colMax[c] = Math.Max(colMax[c], val);
            }
            i = j;
        }
        return ans;
    }
}
