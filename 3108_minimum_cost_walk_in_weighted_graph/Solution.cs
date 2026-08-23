// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

using System.Collections.Generic;

public class Solution {
    class UnionFind {
        int[] p, size;
        public UnionFind(int n) {
            p = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) { p[i] = i; size[i] = 1; }
        }
        public int Find(int x) {
            if (p[x] != x) p[x] = Find(p[x]);
            return p[x];
        }
        public void Unite(int a, int b) {
            int pa = Find(a), pb = Find(b);
            if (pa == pb) return;
            if (size[pa] > size[pb]) { p[pb] = pa; size[pa] += size[pb]; }
            else { p[pa] = pb; size[pb] += size[pa]; }
        }
    }

    public int[] MinimumCost(int n, int[][] edges, int[][] query) {
        var uf = new UnionFind(n);
        int[] g = new int[n];
        for (int i = 0; i < n; i++) g[i] = -1;
        foreach (var e in edges) uf.Unite(e[0], e[1]);
        foreach (var e in edges) {
            int root = uf.Find(e[0]);
            g[root] &= e[2];
        }
        int F(int u, int v) {
            if (u == v) return 0;
            int a = uf.Find(u), b = uf.Find(v);
            if (a == b) return g[a];
            return -1;
        }
        int[] ans = new int[query.Length];
        for (int i = 0; i < query.Length; i++) ans[i] = F(query[i][0], query[i][1]);
        return ans;
    }
}
