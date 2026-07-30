// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

using System.Collections.Generic;

public class Solution {
    public int CountPaths(int n, int[][] roads) {
        const int MOD = 1000000007;
        var g = new List<(int v, long t)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, long)>();
        foreach (var r in roads) {
            g[r[0]].Add((r[1], r[2]));
            g[r[1]].Add((r[0], r[2]));
        }
        var dist = new long[n];
        var ways = new long[n];
        for (int i = 0; i < n; i++) dist[i] = long.MaxValue / 4;
        dist[0] = 0; ways[0] = 1;
        var pq = new PriorityQueue<(long d, int u), long>();
        pq.Enqueue((0, 0), 0);
        while (pq.Count > 0) {
            var (d, u) = pq.Dequeue();
            if (d > dist[u]) continue;
            foreach (var (v, w) in g[u]) {
                long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    ways[v] = ways[u];
                    pq.Enqueue((nd, v), nd);
                } else if (nd == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        return (int)ways[n - 1];
    }
}