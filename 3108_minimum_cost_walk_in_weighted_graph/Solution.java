// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

class Solution {
    static class UnionFind {
        int[] p, size;
        UnionFind(int n) {
            p = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                p[i] = i;
                size[i] = 1;
            }
        }
        int find(int x) {
            if (p[x] != x) p[x] = find(p[x]);
            return p[x];
        }
        void unite(int a, int b) {
            int pa = find(a), pb = find(b);
            if (pa == pb) return;
            if (size[pa] > size[pb]) {
                p[pb] = pa;
                size[pa] += size[pb];
            } else {
                p[pa] = pb;
                size[pb] += size[pa];
            }
        }
    }

    public int[] minimumCost(int n, int[][] edges, int[][] query) {
        UnionFind uf = new UnionFind(n);
        int[] g = new int[n];
        for (int i = 0; i < n; i++) g[i] = -1;
        for (int[] e : edges) uf.unite(e[0], e[1]);
        for (int[] e : edges) {
            int root = uf.find(e[0]);
            g[root] &= e[2];
        }
        int[] ans = new int[query.length];
        for (int i = 0; i < query.length; i++) {
            int u = query[i][0], v = query[i][1];
            if (u == v) ans[i] = 0;
            else {
                int a = uf.find(u), b = uf.find(v);
                ans[i] = (a == b) ? g[a] : -1;
            }
        }
        return ans;
    }
}
