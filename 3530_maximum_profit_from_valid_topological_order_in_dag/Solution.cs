// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

public class Solution {
    int Pop(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }
    public int MaxProfit(int n, int[][] edges, int[] score) {
        int[] need = new int[n], dp = new int[1 << n];
        for (int i = 0; i < dp.Length; i++) dp[i] = -1;
        dp[0] = 0;
        foreach (var e in edges) need[e[1]] |= 1 << e[0];
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] < 0) continue;
            int pos = Pop(mask) + 1;
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) != 0) continue;
                if ((mask & need[i]) == need[i]) {
                    int nm = mask | (1 << i);
                    int v = dp[mask] + score[i] * pos;
                    if (v > dp[nm]) dp[nm] = v;
                }
            }
        }
        return dp[(1 << n) - 1];
    }
}
