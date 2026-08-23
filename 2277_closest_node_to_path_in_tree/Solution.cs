// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] ClosestNode(int n, int[][] edges, int[][] query) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        const int LOG = 17;
        int[,] up = new int[LOG, n];
        int[] depth = new int[n];
        void Dfs(int u, int p) {
            up[0, u] = p;
            foreach (int v in g[u]) if (v != p) { depth[v] = depth[u] + 1; Dfs(v, u); }
        }
        Dfs(0, 0);
        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++) up[k, v] = up[k - 1, up[k - 1, v]];
        int Lift(int v, int d) {
            for (int k = 0; k < LOG; k++) if (((d >> k) & 1) != 0) v = up[k, v];
            return v;
        }
        int Lca(int a, int b) {
            if (depth[a] < depth[b]) { int t = a; a = b; b = t; }
            a = Lift(a, depth[a] - depth[b]);
            if (a == b) return a;
            for (int k = LOG - 1; k >= 0; k--)
                if (up[k, a] != up[k, b]) { a = up[k, a]; b = up[k, b]; }
            return up[0, a];
        }
        int Dist(int a, int b) {
            int c = Lca(a, b);
            return depth[a] + depth[b] - 2 * depth[c];
        }
        int[] ans = new int[query.Length];
        for (int i = 0; i < query.Length; i++) {
            int a = query[i][0], b = query[i][1], x = query[i][2];
            int[] cands = { Lca(a, b), Lca(a, x), Lca(b, x) };
            int best = cands[0], bestD = Dist(cands[0], x);
            for (int t = 1; t < 3; t++) {
                int d = Dist(cands[t], x);
                if (d < bestD) { bestD = d; best = cands[t]; }
            }
            ans[i] = best;
        }
        return ans;
    }
}
