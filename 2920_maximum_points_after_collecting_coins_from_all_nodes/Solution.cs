// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

using System.Collections.Generic;

public class Solution {
    public int MaximumPoints(int[][] edges, int[] coins, int k) {
        int n = coins.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        var memo = new Dictionary<(int, int), int>();
        int Dfs(int u, int p, int shifts) {
            if (shifts > 14) shifts = 14;
            var key = (u, shifts);
            if (memo.ContainsKey(key)) return memo[key];
            int c = coins[u] >> shifts;
            int opt1 = c - k, opt2 = c / 2;
            foreach (int v in g[u]) {
                if (v == p) continue;
                opt1 += Dfs(v, u, shifts);
                opt2 += Dfs(v, u, shifts + 1);
            }
            int best = opt1 > opt2 ? opt1 : opt2;
            return memo[key] = best;
        }
        return Dfs(0, -1, 0);
    }
}
