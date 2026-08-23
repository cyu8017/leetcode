// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

using System.Collections.Generic;

public class Graph {
    List<(int to, int w)>[] g;

    public Graph(int n, int[][] edges) {
        g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) g[e[0]].Add((e[1], e[2]));
    }

    public void AddEdge(int[] edge) {
        g[edge[0]].Add((edge[1], edge[2]));
    }

    public int ShortestPath(int node1, int node2) {
        int n = g.Length;
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = 1 << 30;
        dist[node1] = 0;
        var pq = new PriorityQueue<int, int>();
        pq.Enqueue(node1, 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out int u, out int d);
            if (u == node2) return d;
            if (d > dist[u]) continue;
            foreach (var e in g[u]) {
                int nd = d + e.w;
                if (nd < dist[e.to]) {
                    dist[e.to] = nd;
                    pq.Enqueue(e.to, nd);
                }
            }
        }
        return -1;
    }
}
