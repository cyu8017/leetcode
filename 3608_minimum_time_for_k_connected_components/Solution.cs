// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

using System;

public class Solution {
    class UnionFind {
        int[] p, size;
        public UnionFind(int n) {
            p = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) { p[i] = i; size[i] = 1; }
        }
        public int Find(int x) => p[x] == x ? x : p[x] = Find(p[x]);
        public bool Unite(int a, int b) {
            int pa = Find(a), pb = Find(b);
            if (pa == pb) return false;
            if (size[pa] > size[pb]) { p[pb] = pa; size[pa] += size[pb]; }
            else { p[pa] = pb; size[pb] += size[pa]; }
            return true;
        }
    }
    public int MinTime(int n, int[][] edges, int k) {
        Array.Sort(edges, (a, b) => a[2].CompareTo(b[2]));
        var uf = new UnionFind(n);
        int cnt = n;
        for (int i = edges.Length - 1; i >= 0; i--) {
            if (uf.Unite(edges[i][0], edges[i][1])) {
                cnt--;
                if (cnt < k) return edges[i][2];
            }
        }
        return 0;
    }
}
