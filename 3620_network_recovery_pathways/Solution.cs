// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

using System;
using System.Collections.Generic;

public class Solution {
    public int FindMaxPathScore(int[][] edges, bool[] online, long k) {
        int n = online.Length;
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        int l = int.MaxValue, r = 0;
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            if (!online[u] || !online[v]) continue;
            g[u].Add((v, w));
            l = Math.Min(l, w);
            r = Math.Max(r, w);
        }
        if (l == int.MaxValue) return -1;
        bool Check(int mid) {
            const int INF = int.MaxValue / 2;
            int[] dist = new int[n];
            Array.Fill(dist, INF);
            dist[0] = 0;
            var pq = new PriorityQueue<int, int>();
            pq.Enqueue(0, 0);
            while (pq.Count > 0) {
                pq.TryDequeue(out int u, out int d);
                if ((long)d > k) return false;
                if (u == n - 1) return true;
                if (dist[u] < d) continue;
                foreach (var (v, w) in g[u]) {
                    if (w < mid) continue;
                    int nd = d + w;
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.Enqueue(v, nd);
                    }
                }
            }
            return false;
        }
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (Check(mid)) l = mid;
            else r = mid - 1;
        }
        return Check(l) ? l : -1;
    }
}
