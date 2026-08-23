// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

using System;
using System.Collections.Generic;

public class Solution {
    public int NetworkBecomesIdle(int[][] edges, int[] patience) {
        int n = patience.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        int[] dist = new int[n];
        Array.Fill(dist, -1);
        var q = new Queue<int>();
        q.Enqueue(0); dist[0] = 0;
        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in g[u]) if (dist[v] == -1) { dist[v] = dist[u] + 1; q.Enqueue(v); }
        }
        int ans = 0;
        for (int i = 1; i < n; i++) {
            int round = dist[i] * 2;
            int lastSend = (round - 1) / patience[i] * patience[i];
            ans = Math.Max(ans, lastSend + round);
        }
        return ans + 1;
    }
}
