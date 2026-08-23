// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumDistance(int n, int[][] edges, int s, int[] marked) {
        var g = new List<(int v, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) g[e[0]].Add((e[1], e[2]));
        var mark = new HashSet<int>(marked);
        int[] dist = new int[n];
        Array.Fill(dist, int.MaxValue / 4);
        dist[s] = 0;
        var pq = new PriorityQueue<(int d, int u), int>();
        pq.Enqueue((0, s), 0);
        while (pq.Count > 0) {
            var (d, u) = pq.Dequeue();
            if (mark.Contains(u)) return d;
            if (d > dist[u]) continue;
            foreach (var (v, w) in g[u]) {
                if (d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.Enqueue((dist[v], v), dist[v]);
                }
            }
        }
        return -1;
    }
}
