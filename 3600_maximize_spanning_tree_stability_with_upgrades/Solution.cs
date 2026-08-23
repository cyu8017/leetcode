// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

using System;

public class Solution {
    class UnionFind {
        public int[] p, size;
        public int cnt;
        public UnionFind(int n) {
            p = new int[n];
            size = new int[n];
            cnt = n;
            for (int i = 0; i < n; i++) { p[i] = i; size[i] = 1; }
        }
        public int Find(int x) { return p[x] == x ? x : p[x] = Find(p[x]); }
        public bool Unite(int a, int b) {
            int pa = Find(a), pb = Find(b);
            if (pa == pb) return false;
            if (size[pa] > size[pb]) { p[pb] = pa; size[pa] += size[pb]; }
            else { p[pa] = pb; size[pb] += size[pa]; }
            cnt--;
            return true;
        }
    }

    int N, K;
    int[][] E;

    bool Check(int lim) {
        var uf = new UnionFind(N);
        foreach (var e in E) {
            if (e[2] >= lim) uf.Unite(e[0], e[1]);
        }
        int rem = K;
        foreach (var e in E) {
            if (e[2] * 2 >= lim && rem > 0) {
                if (uf.Unite(e[0], e[1])) rem--;
            }
        }
        return uf.cnt == 1;
    }

    public int MaxStability(int n, int[][] edges, int k) {
        N = n;
        E = edges;
        K = k;
        var uf = new UnionFind(n);
        int mn = 1000000;
        foreach (var e in edges) {
            if (e[3] == 1) {
                mn = Math.Min(mn, e[2]);
                if (!uf.Unite(e[0], e[1])) return -1;
            }
        }
        foreach (var e in edges) uf.Unite(e[0], e[1]);
        if (uf.cnt > 1) return -1;
        int l = 1, r = mn;
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (Check(mid)) l = mid;
            else r = mid - 1;
        }
        return l;
    }
}
