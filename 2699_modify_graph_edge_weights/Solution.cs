// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

using System.Collections.Generic;

public class Solution {
    public int[][] ModifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        const int INF = 2000000000;
        int[] Dijkstra(bool ignoreNeg) {
            int[] dist = new int[n];
            for (int i = 0; i < n; i++) dist[i] = INF;
            dist[source] = 0;
            var pq = new PriorityQueue<int, int>();
            pq.Enqueue(source, 0);
            while (pq.Count > 0) {
                pq.TryDequeue(out int u, out int d);
                if (d != dist[u]) continue;
                for (int i = 0; i < edges.Length; i++) {
                    int a = edges[i][0], b = edges[i][1], w = edges[i][2];
                    if (a != u && b != u) continue;
                    int to = a == u ? b : a;
                    if (w == -1) {
                        if (ignoreNeg) continue;
                        w = 1;
                    }
                    if (d + w < dist[to]) {
                        dist[to] = d + w;
                        pq.Enqueue(to, dist[to]);
                    }
                }
            }
            return dist;
        }
        var d = Dijkstra(true);
        if (d[destination] < target) return new int[0][];
        bool matched = d[destination] == target;
        for (int i = 0; i < edges.Length; i++) {
            if (edges[i][2] != -1) continue;
            if (matched) { edges[i][2] = INF; continue; }
            edges[i][2] = 1;
            d = Dijkstra(false);
            if (d[destination] <= target) {
                edges[i][2] += target - d[destination];
                matched = true;
            }
        }
        d = Dijkstra(false);
        if (d[destination] != target) return new int[0][];
        return edges;
    }
}
