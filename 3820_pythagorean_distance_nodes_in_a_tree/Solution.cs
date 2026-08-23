// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

using System;
using System.Collections.Generic;

public class Solution {
    public int SpecialNodes(int n, int[][] edges, int x, int y, int z) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        const int INF = 1000000000;
        int[] Bfs(int start) {
            int[] dist = new int[n];
            for (int i = 0; i < n; i++) dist[i] = INF;
            var q = new Queue<int>();
            dist[start] = 0;
            q.Enqueue(start);
            while (q.Count > 0) {
                int u = q.Dequeue();
                foreach (int v in g[u]) {
                    if (dist[v] > dist[u] + 1) {
                        dist[v] = dist[u] + 1;
                        q.Enqueue(v);
                    }
                }
            }
            return dist;
        }
        int[] d1 = Bfs(x), d2 = Bfs(y), d3 = Bfs(z);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int[] a = { d1[i], d2[i], d3[i] };
            Array.Sort(a);
            long x0 = a[0], x1 = a[1], x2 = a[2];
            if (x0 * x0 + x1 * x1 == x2 * x2) ans++;
        }
        return ans;
    }
}
