// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

using System.Collections.Generic;

public class Solution {
    public int[] LastMarkedNodes(int[][] edges) {
        int n = edges.Length + 1;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        (int far, int[] dist) Bfs(int start) {
            int[] dist = new int[n];
            for (int i = 0; i < n; i++) dist[i] = -1;
            var q = new Queue<int>();
            q.Enqueue(start);
            dist[start] = 0;
            int far = start;
            while (q.Count > 0) {
                int u = q.Dequeue();
                if (dist[u] > dist[far]) far = u;
                foreach (int v in g[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.Enqueue(v);
                    }
                }
            }
            return (far, dist);
        }
        var (u, _) = Bfs(0);
        var (v, du) = Bfs(u);
        var (__, dv) = Bfs(v);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = du[i] >= dv[i] ? u : v;
        return ans;
    }
}
