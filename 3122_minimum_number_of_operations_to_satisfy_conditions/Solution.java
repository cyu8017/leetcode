// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

import java.util.Arrays;

class Solution {
    public int minimumOperations(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        final int INF = 1 << 29;
        int[][] f = new int[n][10];
        for (int[] row : f) Arrays.fill(row, INF);
        for (int i = 0; i < n; i++) {
            int[] cnt = new int[10];
            for (int j = 0; j < m; j++) cnt[grid[j][i]]++;
            if (i == 0) {
                for (int j = 0; j < 10; j++) f[i][j] = m - cnt[j];
            } else {
                for (int j = 0; j < 10; j++) {
                    for (int k = 0; k < 10; k++) {
                        if (j != k) f[i][j] = Math.min(f[i][j], f[i - 1][k] + m - cnt[j]);
                    }
                }
            }
        }
        int ans = INF;
        for (int j = 0; j < 10; j++) ans = Math.min(ans, f[n - 1][j]);
        return ans;
    }
}
