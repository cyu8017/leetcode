// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

using System;

public class Solution {
    public int MaxScore(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        const int Inf = 1 << 30;
        int[][] f = new int[m][];
        for (int i = 0; i < m; i++) f[i] = new int[n];
        int ans = -Inf;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int x = grid[i][j];
                int mi = Inf;
                if (i > 0) mi = Math.Min(mi, f[i - 1][j]);
                if (j > 0) mi = Math.Min(mi, f[i][j - 1]);
                ans = Math.Max(ans, x - mi);
                f[i][j] = Math.Min(x, mi);
            }
        }
        return ans;
    }
}
