// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

using System.Collections.Generic;

public class Solution {
    public int ShortestPathWithHops(int n, int[][] edges, int s, int d, int k) {
        var g = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        int[][] dist = new int[n][];
        for (int i = 0; i < n; i++) {
            dist[i] = new int[k + 1];
            for (int j = 0; j <= k; j++) dist[i][j] = int.MaxValue / 4;
        }
        dist[s][0] = 0;
        var pq = new PriorityQueue<(int u, int hops), int>();
        pq.Enqueue((s, 0), 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out var state, out int cd);
            int u = state.u, hops = state.hops;
            if (u == d) return cd;
            if (cd > dist[u][hops]) continue;
            foreach (var (to, w) in g[u]) {
                if (cd + w < dist[to][hops]) {
                    dist[to][hops] = cd + w;
                    pq.Enqueue((to, hops), dist[to][hops]);
                }
                if (hops < k && cd < dist[to][hops + 1]) {
                    dist[to][hops + 1] = cd;
                    pq.Enqueue((to, hops + 1), cd);
                }
            }
        }
        return -1;
    }
}
