// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumTotalPrice(int n, int[][] edges, int[] price, int[][] trips) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        int[] cnt = new int[n];
        bool Path(int u, int p, int target) {
            if (u == target) { cnt[u]++; return true; }
            foreach (int v in g[u]) {
                if (v == p) continue;
                if (Path(v, u, target)) { cnt[u]++; return true; }
            }
            return false;
        }
        foreach (var t in trips) Path(t[0], -1, t[1]);
        (int full, int half) Dfs(int u, int p) {
            int full = price[u] * cnt[u], half = full / 2;
            foreach (int v in g[u]) {
                if (v == p) continue;
                var (nf, hf) = Dfs(v, u);
                full += Math.Min(nf, hf);
                half += nf;
            }
            return (full, half);
        }
        var (a, b) = Dfs(0, -1);
        return Math.Min(a, b);
    }
}
