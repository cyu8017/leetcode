// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinCost(int maxTime, int[][] edges, int[] passingFee) {
        int n = passingFee.Length;
        var graph = new List<(int v, int t)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            graph[e[0]].Add((e[1], e[2]));
            graph[e[1]].Add((e[0], e[2]));
        }
        var minTime = new int[n];
        Array.Fill(minTime, maxTime + 1);
        var pq = new PriorityQueue<(int cost, int time, int u), int>();
        pq.Enqueue((passingFee[0], 0, 0), passingFee[0]);
        while (pq.Count > 0) {
            var (cost, time, u) = pq.Dequeue();
            if (time >= minTime[u]) continue;
            minTime[u] = time;
            if (u == n - 1) return cost;
            foreach (var (v, dt) in graph[u]) {
                int nt = time + dt;
                if (nt <= maxTime && nt < minTime[v])
                    pq.Enqueue((cost + passingFee[v], nt, v), cost + passingFee[v]);
            }
        }
        return -1;
    }
}