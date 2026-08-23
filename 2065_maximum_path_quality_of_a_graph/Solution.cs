// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximalPathQuality(int[] values, int[][] edges, int maxTime) {
        int n = values.Length;
        var g = new List<(int v, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        int ans = 0;
        int[] vis = new int[n];
        void Dfs(int u, int time, int quality) {
            if (time > maxTime) return;
            bool first = vis[u] == 0;
            if (first) quality += values[u];
            vis[u]++;
            if (u == 0) ans = Math.Max(ans, quality);
            foreach (var (v, w) in g[u]) Dfs(v, time + w, quality);
            vis[u]--;
        }
        Dfs(0, 0, 0);
        return ans;
    }
}
