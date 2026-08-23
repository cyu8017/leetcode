// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumCost(int[] start, int[] target, int[][] specialRoads) {
        var points = new List<int[]> { start, target };
        foreach (var r in specialRoads) {
            points.Add(new int[] { r[0], r[1] });
            points.Add(new int[] { r[2], r[3] });
        }
        int N = points.Count;
        int DistMan(int[] a, int[] b) => Math.Abs(a[0] - b[0]) + Math.Abs(a[1] - b[1]);
        var g = new List<(int to, int w)>[N];
        for (int i = 0; i < N; i++) g[i] = new List<(int, int)>();
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (i != j) g[i].Add((j, DistMan(points[i], points[j])));
        foreach (var r in specialRoads) {
            int u = -1, v = -1;
            for (int i = 0; i < N; i++) {
                if (points[i][0] == r[0] && points[i][1] == r[1]) u = i;
                if (points[i][0] == r[2] && points[i][1] == r[3]) v = i;
            }
            if (u >= 0 && v >= 0) g[u].Add((v, r[4]));
        }
        int[] dist = new int[N];
        for (int i = 0; i < N; i++) dist[i] = int.MaxValue / 4;
        dist[0] = 0;
        var pq = new PriorityQueue<int, int>();
        pq.Enqueue(0, 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out int id, out int cost);
            if (cost > dist[id]) continue;
            foreach (var (to, w) in g[id]) {
                if (cost + w < dist[to]) {
                    dist[to] = cost + w;
                    pq.Enqueue(to, dist[to]);
                }
            }
        }
        return dist[1];
    }
}
