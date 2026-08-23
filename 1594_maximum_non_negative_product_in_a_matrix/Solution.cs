// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

using System;

public class Solution {
    public int MaxProductPath(int[][] grid) {
        const int MOD = 1000000007;
        int m = grid.Length, n = grid[0].Length;
        long[,] high = new long[m, n];
        long[,] low = new long[m, n];
        high[0, 0] = low[0, 0] = grid[0][0];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (r == 0 && c == 0) continue;
                long maxVal = long.MinValue, minVal = long.MaxValue;
                if (r > 0) {
                    maxVal = Math.Max(maxVal, Math.Max(high[r - 1, c] * grid[r][c], low[r - 1, c] * grid[r][c]));
                    minVal = Math.Min(minVal, Math.Min(high[r - 1, c] * grid[r][c], low[r - 1, c] * grid[r][c]));
                }
                if (c > 0) {
                    maxVal = Math.Max(maxVal, Math.Max(high[r, c - 1] * grid[r][c], low[r, c - 1] * grid[r][c]));
                    minVal = Math.Min(minVal, Math.Min(high[r, c - 1] * grid[r][c], low[r, c - 1] * grid[r][c]));
                }
                high[r, c] = maxVal;
                low[r, c] = minVal;
            }
        }
        return high[m - 1, n - 1] >= 0 ? (int)(high[m - 1, n - 1] % MOD) : -1;
    }
}
