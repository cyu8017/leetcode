// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

using System;
using System.Collections.Generic;

public class Solution {
    public int NetworkDelayTime(int[][] times, int n, int k) {
        var graph = new List<(int, int)>[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new List<(int, int)>();
        foreach (var edge in times) graph[edge[0]].Add((edge[1], edge[2]));
        const int INF = int.MaxValue / 4;
        int[] dist = new int[n + 1];
        Array.Fill(dist, INF);
        dist[k] = 0;
        var heap = new PriorityQueue<(int d, int node), int>();
        heap.Enqueue((0, k), 0);
        while (heap.Count > 0) {
            var (d, node) = heap.Dequeue();
            if (d > dist[node]) continue;
            foreach (var (nei, weight) in graph[node]) {
                int nd = d + weight;
                if (nd < dist[nei]) {
                    dist[nei] = nd;
                    heap.Enqueue((nd, nei), nd);
                }
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = Math.Max(ans, dist[i]);
        return ans == INF ? -1 : ans;
    }
}
