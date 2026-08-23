// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

using System.Collections.Generic;

public class Solution {
    public long ShortestPath(int n, int[][] edges, string labels, int k) {
        var graph = new List<(int to, int weight)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var edge in edges) graph[edge[0]].Add((edge[1], edge[2]));
        const long infinity = long.MaxValue / 4;
        long[][] distances = new long[n][];
        for (int i = 0; i < n; i++) {
            distances[i] = new long[k + 1];
            for (int j = 0; j <= k; j++) distances[i][j] = infinity;
        }
        distances[0][1] = 0;
        var pq = new PriorityQueue<(int node, int run), long>();
        pq.Enqueue((0, 1), 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out var state, out long distance);
            int node = state.node, run = state.run;
            if (distance != distances[node][run]) continue;
            if (node == n - 1) return distance;
            foreach (var (to, weight) in graph[node]) {
                int nextRun = 1;
                if (labels[node] == labels[to]) nextRun = run + 1;
                if (nextRun > k) continue;
                long nextDistance = distance + weight;
                if (nextDistance < distances[to][nextRun]) {
                    distances[to][nextRun] = nextDistance;
                    pq.Enqueue((to, nextRun), nextDistance);
                }
            }
        }
        return -1;
    }
}
