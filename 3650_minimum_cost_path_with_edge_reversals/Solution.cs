// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

using System.Collections.Generic;

public class Solution {
    public int MinCost(int n, int[][] edges) {
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].Add((v, w));
            g[v].Add((u, w * 2));
        }
        const int inf = int.MaxValue / 2;
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = inf;
        dist[0] = 0;
        var pq = new PriorityQueue<int, int>();
        pq.Enqueue(0, 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out int u, out int d);
            if (d > dist[u]) continue;
            if (u == n - 1) return d;
            foreach (var (v, w) in g[u]) {
                int nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.Enqueue(v, nd);
                }
            }
        }
        return -1;
    }
}
