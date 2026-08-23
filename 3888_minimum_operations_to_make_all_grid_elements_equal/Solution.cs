// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

using System;

public class Solution {
    public long MinOperations(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        int maxVal = grid[0][0];
        foreach (var row in grid) foreach (int x in row) maxVal = Math.Max(maxVal, x);

        long Check(int target) {
            var diff = new long[m + 2][];
            for (int i = 0; i < m + 2; i++) diff[i] = new long[n + 2];
            long totalOps = 0;
            for (int i = 1; i <= m; i++) {
                for (int j = 1; j <= n; j++) {
                    diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
                    long curVal = (long)grid[i - 1][j - 1] + diff[i][j];
                    if (curVal > target) return -1;
                    if (curVal < target) {
                        if (i + k - 1 > m || j + k - 1 > n) return -1;
                        long needed = target - curVal;
                        totalOps += needed;
                        diff[i][j] += needed;
                        diff[i + k][j] -= needed;
                        diff[i][j + k] -= needed;
                        diff[i + k][j + k] += needed;
                    }
                }
            }
            return totalOps;
        }

        for (int t = maxVal; t <= maxVal + 1; t++) {
            long res = Check(t);
            if (res != -1) return res;
        }
        return -1;
    }
}
