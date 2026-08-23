// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

import java.util.Arrays;

class Solution {
    static class UnionFind {
        int[] p, size;
        UnionFind(int n) {
            p = new int[n];
            size = new int[n];
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
            return true;
        }
    }

    public int minTime(int n, int[][] edges, int k) {
        Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));
        UnionFind uf = new UnionFind(n);
        int cnt = n;
        for (int i = edges.length - 1; i >= 0; i--) {
            if (uf.unite(edges[i][0], edges[i][1])) {
                cnt--;
                if (cnt < k) return edges[i][2];
            }
        }
        return 0;
    }
}
