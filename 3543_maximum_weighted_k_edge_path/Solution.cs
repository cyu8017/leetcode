// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

using System.Collections.Generic;

public class Solution {
    public int MaxWeight(int n, int[][] edges, int k, int t) {
        var graph = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) graph[e[0]].Add((e[1], e[2]));
        var dp = new HashSet<int>[n][];
        for (int u = 0; u < n; u++) {
            dp[u] = new HashSet<int>[k + 1];
            for (int i = 0; i <= k; i++) dp[u][i] = new HashSet<int>();
        }
        for (int u = 0; u < n; u++) dp[u][0].Add(0);
        for (int i = 0; i < k; i++) {
            for (int u = 0; u < n; u++) {
                foreach (int sum in dp[u][i]) {
                    foreach (var (to, w) in graph[u]) {
                        int ns = sum + w;
                        if (ns < t) dp[to][i + 1].Add(ns);
                    }
                }
            }
        }
        int ans = -1;
        for (int u = 0; u < n; u++)
            foreach (int sum in dp[u][k]) if (sum > ans) ans = sum;
        return ans;
    }
}
