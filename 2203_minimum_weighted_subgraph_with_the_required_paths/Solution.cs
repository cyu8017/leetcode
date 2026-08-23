// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

using System;
using System.Collections.Generic;

public class Solution {
    long[] Dijkstra(int n, List<(int, int)>[] g, int src) {
        const long INF = 1L << 62;
        long[] dist = new long[n];
        Array.Fill(dist, INF);
        dist[src] = 0;
        var pq = new PriorityQueue<int, long>();
        pq.Enqueue(src, 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out int u, out long d);
            if (d != dist[u]) continue;
            foreach (var (v, w) in g[u]) {
                if (d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.Enqueue(v, dist[v]);
                }
            }
        }
        return dist;
    }

    public long MinimumWeight(int n, int[][] edges, int src1, int src2, int dest) {
        var g = new List<(int, int)>[n];
        var rg = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) { g[i] = new List<(int, int)>(); rg[i] = new List<(int, int)>(); }
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            rg[e[1]].Add((e[0], e[2]));
        }
        long[] d1 = Dijkstra(n, g, src1);
        long[] d2 = Dijkstra(n, g, src2);
        long[] dd = Dijkstra(n, rg, dest);
        const long INF = 1L << 62;
        long ans = INF;
        for (int i = 0; i < n; i++) {
            if (d1[i] >= INF || d2[i] >= INF || dd[i] >= INF) continue;
            ans = Math.Min(ans, d1[i] + d2[i] + dd[i]);
        }
        return ans >= INF ? -1 : ans;
    }
}
