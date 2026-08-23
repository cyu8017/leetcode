// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

using System.Collections.Generic;

public class Solution {
    public long[] MinCost(int n, int[][] roads, int[] appleCost, int k) {
        var g = new List<(int v, int w)>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<(int, int)>();
        foreach (var r in roads) {
            g[r[0]].Add((r[1], r[2]));
            g[r[1]].Add((r[0], r[2]));
        }
        long[] ans = new long[n];
        const long INF = 1L << 60;
        for (int start = 1; start <= n; start++) {
            long[] dist = new long[n + 1];
            for (int i = 0; i <= n; i++) dist[i] = INF;
            dist[start] = 0;
            var pq = new PriorityQueue<(long d, int u), long>();
            pq.Enqueue((0, start), 0);
            while (pq.Count > 0) {
                var (d, u) = pq.Dequeue();
                if (d != dist[u]) continue;
                foreach (var (v, w) in g[u]) {
                    long nd = d + w;
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.Enqueue((nd, v), nd);
                    }
                }
            }
            long best = INF;
            for (int city = 1; city <= n; city++) {
                long cost = dist[city] * (k + 1) + appleCost[city - 1];
                if (cost < best) best = cost;
            }
            ans[start - 1] = best;
        }
        return ans;
    }
}
