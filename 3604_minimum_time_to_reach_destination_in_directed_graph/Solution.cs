// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

using System.Collections.Generic;

public class Solution {
    public int MinTime(int n, int[][] edges) {
        var g = new List<(int to, int start, int end)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int, int)>();
        foreach (var e in edges) g[e[0]].Add((e[1], e[2], e[3]));
        const long Inf = (long)1e18;
        long[] dist = new long[n];
        for (int i = 0; i < n; i++) dist[i] = Inf;
        dist[0] = 0;
        var pq = new PriorityQueue<int, long>();
        pq.Enqueue(0, 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out int u, out long t);
            if (t != dist[u]) continue;
            if (u == n - 1) return (int)t;
            foreach (var e in g[u]) {
                long nt = t;
                if (nt > e.end) continue;
                if (nt < e.start) nt = e.start;
                nt += 1;
                if (nt < dist[e.to]) {
                    dist[e.to] = nt;
                    pq.Enqueue(e.to, nt);
                }
            }
        }
        return dist[n - 1] == Inf ? -1 : (int)dist[n - 1];
    }
}
