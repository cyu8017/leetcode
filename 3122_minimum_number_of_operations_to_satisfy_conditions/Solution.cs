// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

using System;

public class Solution {
    public int MinimumOperations(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        const int Inf = 1 << 29;
        int[][] f = new int[n][];
        for (int i = 0; i < n; i++) {
            f[i] = new int[10];
            for (int j = 0; j < 10; j++) f[i][j] = Inf;
        }
        for (int i = 0; i < n; i++) {
            int[] cnt = new int[10];
            for (int j = 0; j < m; j++) cnt[grid[j][i]]++;
            if (i == 0) {
                for (int j = 0; j < 10; j++) f[i][j] = m - cnt[j];
            } else {
                for (int j = 0; j < 10; j++) {
                    for (int k = 0; k < 10; k++) {
                        if (j != k) f[i][j] = Math.Min(f[i][j], f[i - 1][k] + m - cnt[j]);
                    }
                }
            }
        }
        int ans = Inf;
        for (int j = 0; j < 10; j++) ans = Math.Min(ans, f[n - 1][j]);
        return ans;
    }
}
