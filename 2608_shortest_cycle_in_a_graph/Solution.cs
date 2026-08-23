// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

using System.Collections.Generic;

public class Solution {
    public int FindShortestCycle(int n, int[][] edges) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        const int INF = 1000000000;
        int ans = INF;
        for (int start = 0; start < n; ++start) {
            int[] dist = new int[n];
            int[] parent = new int[n];
            for (int i = 0; i < n; i++) { dist[i] = -1; parent[i] = -1; }
            var q = new Queue<int>();
            q.Enqueue(start);
            dist[start] = 0;
            while (q.Count > 0) {
                int u = q.Dequeue();
                foreach (int v in g[u]) {
                    if (dist[v] < 0) {
                        dist[v] = dist[u] + 1;
                        parent[v] = u;
                        q.Enqueue(v);
                    } else if (parent[u] != v) {
                        int c = dist[u] + dist[v] + 1;
                        if (c < ans) ans = c;
                    }
                }
            }
        }
        return ans == INF ? -1 : ans;
    }
}
