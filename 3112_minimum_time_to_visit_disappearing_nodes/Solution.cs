// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

using System.Collections.Generic;

public class Solution {
    public int[] MinimumTime(int n, int[][] edges, int[] disappear) {
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        const int INF = 1 << 30;
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[0] = 0;
        var pq = new PriorityQueue<int, int>();
        pq.Enqueue(0, 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out int u, out int du);
            if (du > dist[u]) continue;
            foreach (var (v, w) in g[u]) {
                if (dist[v] > dist[u] + w && dist[u] + w < disappear[v]) {
                    dist[v] = dist[u] + w;
                    pq.Enqueue(v, dist[v]);
                }
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++)
            ans[i] = dist[i] < disappear[i] ? dist[i] : -1;
        return ans;
    }
}
