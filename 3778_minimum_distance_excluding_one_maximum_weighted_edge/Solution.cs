// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

using System;
using System.Collections.Generic;

public class Solution {
    public long MinCostExcludingMax(int n, int[][] edges) {
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].Add((v, w));
            g[v].Add((u, w));
        }
        const long INF = (long)4e18;
        long[,] dist = new long[n, 2];
        for (int i = 0; i < n; i++) { dist[i, 0] = INF; dist[i, 1] = INF; }
        dist[0, 0] = 0;
        var pq = new PriorityQueue<(long cur, int u, int used), long>();
        pq.Enqueue((0, 0, 0), 0);
        while (pq.Count > 0) {
            var (cur, u, used) = pq.Dequeue();
            if (cur > dist[u, used]) continue;
            if (u == n - 1 && used == 1) return cur;
            foreach (var (v, w) in g[u]) {
                long nxt = cur + w;
                if (nxt < dist[v, used]) {
                    dist[v, used] = nxt;
                    pq.Enqueue((nxt, v, used), nxt);
                }
                if (used == 0) {
                    nxt = cur;
                    if (nxt < dist[v, 1]) {
                        dist[v, 1] = nxt;
                        pq.Enqueue((nxt, v, 1), nxt);
                    }
                }
            }
        }
        return dist[n - 1, 1];
    }
}
