// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int maximumCost(int n, int[][] highways, int k) {
        if (k + 1 > n) return -1;
        @SuppressWarnings("unchecked")
        List<int[]>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] h : highways) {
            g[h[0]].add(new int[] { h[1], h[2] });
            g[h[1]].add(new int[] { h[0], h[2] });
        }
        int[][] dp = new int[1 << n][n];
        for (int i = 0; i < (1 << n); i++)
            for (int j = 0; j < n; j++)
                dp[i][j] = -1;
        for (int i = 0; i < n; i++) dp[1 << i][i] = 0;
        int ans = -1;
        for (int mask = 0; mask < (1 << n); mask++) {
            int cities = Integer.bitCount(mask);
            for (int u = 0; u < n; u++) {
                if (dp[mask][u] < 0) continue;
                if (cities - 1 == k) ans = Math.max(ans, dp[mask][u]);
                for (int[] e : g[u]) {
                    int v = e[0], w = e[1];
                    if ((mask & (1 << v)) != 0) continue;
                    int nm = mask | (1 << v);
                    dp[nm][v] = Math.max(dp[nm][v], dp[mask][u] + w);
                }
            }
        }
        return ans;
    }
}
