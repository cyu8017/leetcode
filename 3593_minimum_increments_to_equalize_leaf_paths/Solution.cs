// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinIncrease(int n, int[][] edges, int[] cost) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        int ans = 0;
        long Dfs(int u, int p) {
            if (graph[u].Count == 1 && p != -1) return cost[u];
            var childVals = new List<long>();
            foreach (int v in graph[u]) {
                if (v == p) continue;
                childVals.Add(Dfs(v, u));
            }
            if (childVals.Count == 0) return cost[u];
            long mx = 0;
            foreach (long c in childVals) mx = Math.Max(mx, c);
            foreach (long c in childVals)
                if (c < mx) ans++;
            return mx + cost[u];
        }
        Dfs(0, -1);
        return ans;
    }
}
