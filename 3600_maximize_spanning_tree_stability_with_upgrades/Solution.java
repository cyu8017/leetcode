// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

class Solution {
    static class UnionFind {
        int[] p, size;
        int cnt;
        UnionFind(int n) {
            p = new int[n];
            size = new int[n];
            cnt = n;
            for (int i = 0; i < n; i++) { p[i] = i; size[i] = 1; }
        }
        int find(int x) {
            if (p[x] != x) p[x] = find(p[x]);
            return p[x];
        }
        boolean unite(int a, int b) {
            int pa = find(a), pb = find(b);
            if (pa == pb) return false;
            if (size[pa] > size[pb]) {
                p[pb] = pa;
                size[pa] += size[pb];
            } else {
                p[pa] = pb;
                size[pb] += size[pa];
            }
            cnt--;
            return true;
        }
    }

    int N, K;
    int[][] E;

    boolean check(int lim) {
        UnionFind uf = new UnionFind(N);
        for (int[] e : E) if (e[2] >= lim) uf.unite(e[0], e[1]);
        int rem = K;
        for (int[] e : E) {
            if (e[2] * 2 >= lim && rem > 0) {
                if (uf.unite(e[0], e[1])) rem--;
            }
        }
        return uf.cnt == 1;
    }

    public int maxStability(int n, int[][] edges, int k) {
        N = n;
        E = edges;
        K = k;
        UnionFind uf = new UnionFind(n);
        int mn = 1000000;
        for (int[] e : edges) {
            if (e[3] == 1) {
                mn = Math.min(mn, e[2]);
                if (!uf.unite(e[0], e[1])) return -1;
            }
        }
        for (int[] e : edges) uf.unite(e[0], e[1]);
        if (uf.cnt > 1) return -1;
        int l = 1, r = mn;
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (check(mid)) l = mid;
            else r = mid - 1;
        }
        return l;
    }
}
