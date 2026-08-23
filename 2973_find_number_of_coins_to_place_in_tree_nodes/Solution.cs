// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

using System;
using System.Collections.Generic;

public class Solution {
    public long[] PlacedCoins(int[][] edges, int[] cost) {
        int n = cost.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        long[] ans = new long[n];
        List<int> Dfs(int u, int p) {
            var vals = new List<int> { cost[u] };
            foreach (int v in g[u]) {
                if (v == p) continue;
                vals.AddRange(Dfs(v, u));
            }
            vals.Sort();
            if (vals.Count < 3) {
                ans[u] = 1;
            } else {
                int m = vals.Count;
                long cand1 = (long)vals[m - 1] * vals[m - 2] * vals[m - 3];
                long cand2 = (long)vals[0] * vals[1] * vals[m - 1];
                long best = Math.Max(cand1, cand2);
                if (best < 0) best = 0;
                ans[u] = best;
            }
            if (vals.Count <= 5) return vals;
            return new List<int> { vals[0], vals[1], vals[vals.Count - 3], vals[vals.Count - 2], vals[vals.Count - 1] };
        }
        Dfs(0, -1);
        return ans;
    }
}
