// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public int MaximumCost(int n, int[][] highways, int k) {
        if (k + 1 > n) return -1;
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var h in highways) {
            g[h[0]].Add((h[1], h[2]));
            g[h[1]].Add((h[0], h[2]));
        }
        int[,] dp = new int[1 << n, n];
        for (int i = 0; i < (1 << n); i++)
            for (int j = 0; j < n; j++)
                dp[i, j] = -1;
        for (int i = 0; i < n; i++) dp[1 << i, i] = 0;
        int ans = -1;
        for (int mask = 0; mask < (1 << n); mask++) {
            int cities = BitOperations.PopCount((uint)mask);
            for (int u = 0; u < n; u++) {
                if (dp[mask, u] < 0) continue;
                if (cities - 1 == k) ans = Math.Max(ans, dp[mask, u]);
                foreach (var (v, w) in g[u]) {
                    if ((mask & (1 << v)) != 0) continue;
                    int nm = mask | (1 << v);
                    dp[nm, v] = Math.Max(dp[nm, v], dp[mask, u] + w);
                }
            }
        }
        return ans;
    }
}
