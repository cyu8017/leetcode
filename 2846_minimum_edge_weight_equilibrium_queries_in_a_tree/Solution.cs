// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] MinOperationsQueries(int n, int[][] edges, int[][] queries) {
        var g = new List<(int v, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        const int LOG = 15;
        int[][] up = new int[LOG][];
        for (int j = 0; j < LOG; j++) up[j] = new int[n];
        int[] depth = new int[n];
        int[][] cnt = new int[n][];
        for (int i = 0; i < n; i++) cnt[i] = new int[27];

        void Dfs(int u, int p) {
            up[0][u] = p;
            foreach (var (v, w) in g[u]) {
                if (v == p) continue;
                depth[v] = depth[u] + 1;
                Array.Copy(cnt[u], cnt[v], 27);
                cnt[v][w]++;
                Dfs(v, u);
            }
        }
        Dfs(0, 0);
        for (int j = 1; j < LOG; j++)
            for (int i = 0; i < n; i++) up[j][i] = up[j - 1][up[j - 1][i]];

        int Lca(int a, int b) {
            if (depth[a] < depth[b]) { int t = a; a = b; b = t; }
            int diff = depth[a] - depth[b];
            for (int j = 0; j < LOG; j++) if ((diff & (1 << j)) != 0) a = up[j][a];
            if (a == b) return a;
            for (int j = LOG - 1; j >= 0; j--) {
                if (up[j][a] != up[j][b]) { a = up[j][a]; b = up[j][b]; }
            }
            return up[0][a];
        }

        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int a = queries[i][0], b = queries[i][1];
            int c = Lca(a, b);
            int total = depth[a] + depth[b] - 2 * depth[c];
            int best = 0;
            for (int w = 1; w <= 26; w++) {
                int f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w];
                best = Math.Max(best, f);
            }
            ans[i] = total - best;
        }
        return ans;
    }
}
