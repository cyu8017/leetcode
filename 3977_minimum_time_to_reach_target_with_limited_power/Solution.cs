// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

using System.Collections.Generic;

public class Solution {
    public long[] MinTimeMaxPower(int n, int[][] edges, int power, int[] cost, int source, int target) {
        const long INF = 1L << 62;
        var g = new List<(int to, int t)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) g[e[0]].Add((e[1], e[2]));
        long[][] dist = new long[n][];
        for (int i = 0; i < n; i++) {
            dist[i] = new long[power + 1];
            for (int j = 0; j <= power; j++) dist[i][j] = INF;
        }
        var pq = new PriorityQueue<(int u, int p), (long d, int negP)>();
        pq.Enqueue((source, power), (0, -power));
        dist[source][power] = 0;
        while (pq.Count > 0) {
            pq.TryDequeue(out var state, out var pri);
            long d = pri.d;
            int u = state.u, p = state.p;
            if (u == target) return new long[] { d, p };
            if (d > dist[u][p] || p < cost[u]) continue;
            p -= cost[u];
            foreach (var (v, t) in g[u]) {
                long nd = d + t;
                if (nd < dist[v][p]) {
                    dist[v][p] = nd;
                    pq.Enqueue((v, p), (nd, -p));
                }
            }
        }
        return new long[] { -1, -1 };
    }
}
