// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] TreeQueries(int n, int[][] edges, int[][] queries) {
        var g = new List<(int to, int w)>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<(int, int)>();
        var weight = new Dictionary<(int, int), int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].Add((v, w));
            g[v].Add((u, w));
            int a = Math.Min(u, v), b = Math.Max(u, v);
            weight[(a, b)] = w;
        }
        int[] inT = new int[n + 1], outT = new int[n + 1], dist = new int[n + 1], parent = new int[n + 1];
        int time = 0;
        void Dfs(int u, int p) {
            inT[u] = time++;
            foreach (var (to, w) in g[u]) {
                if (to == p) continue;
                parent[to] = u;
                dist[to] = dist[u] + w;
                Dfs(to, u);
            }
            outT[u] = time - 1;
        }
        Dfs(1, 0);
        int[] bit = new int[n + 2];
        void Add(int i, int v) {
            for (; i <= n; i += i & -i) bit[i] += v;
        }
        void RangeAdd(int l, int r, int v) {
            Add(l + 1, v);
            Add(r + 2, -v);
        }
        int Point(int i) {
            int s = 0;
            for (i++; i > 0; i -= i & -i) s += bit[i];
            return s;
        }
        for (int i = 1; i <= n; i++) RangeAdd(inT[i], inT[i], dist[i]);
        var ans = new List<int>();
        foreach (var q in queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], nw = q[3];
                int a = Math.Min(u, v), b = Math.Max(u, v);
                int ow = weight[(a, b)];
                int delta = nw - ow;
                weight[(a, b)] = nw;
                int child = (parent[u] == v) ? u : v;
                RangeAdd(inT[child], outT[child], delta);
            } else {
                ans.Add(Point(inT[q[1]]));
            }
        }
        return ans.ToArray();
    }
}
