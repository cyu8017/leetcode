// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

using System.Collections.Generic;

public class Solution {
    public bool[] FindAnswer(int n, int[][] edges) {
        var g = new List<int[]>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int[]>();
        for (int i = 0; i < edges.Length; i++) {
            int a = edges[i][0], b = edges[i][1], w = edges[i][2];
            g[a].Add(new[] { b, w, i });
            g[b].Add(new[] { a, w, i });
        }
        const int Inf = 1 << 30;
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = Inf;
        dist[0] = 0;
        var pq = new PriorityQueue<int, int>();
        pq.Enqueue(0, 0);
        while (pq.Count > 0) {
            pq.TryDequeue(out int a, out int da);
            if (da > dist[a]) continue;
            foreach (var e in g[a]) {
                int b = e[0], w = e[1];
                if (dist[b] > dist[a] + w) {
                    dist[b] = dist[a] + w;
                    pq.Enqueue(b, dist[b]);
                }
            }
        }
        bool[] ans = new bool[edges.Length];
        if (dist[n - 1] == Inf) return ans;
        var q = new Queue<int>();
        q.Enqueue(n - 1);
        while (q.Count > 0) {
            int a = q.Dequeue();
            foreach (var e in g[a]) {
                int b = e[0], w = e[1], i = e[2];
                if (dist[a] == dist[b] + w) {
                    ans[i] = true;
                    q.Enqueue(b);
                }
            }
        }
        return ans;
    }
}
