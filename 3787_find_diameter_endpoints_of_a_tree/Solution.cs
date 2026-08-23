// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

using System.Collections.Generic;

public class Solution {
    public string FindSpecialNodes(int n, int[][] edges) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        (int far, int[] dist) Bfs(int start) {
            int[] dist = new int[n];
            for (int i = 0; i < n; i++) dist[i] = -1;
            dist[start] = 0;
            var q = new List<int> { start };
            int far = start;
            for (int head = 0; head < q.Count; head++) {
                int u = q[head];
                if (dist[u] > dist[far]) far = u;
                foreach (int v in g[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.Add(v);
                    }
                }
            }
            return (far, dist);
        }
        var (a, _) = Bfs(0);
        var (b, dist1) = Bfs(a);
        var (__, dist2) = Bfs(b);
        int d = dist1[b];
        char[] ans = new char[n];
        for (int i = 0; i < n; i++) {
            ans[i] = (dist1[i] == d || dist2[i] == d) ? '1' : '0';
        }
        return new string(ans);
    }
}
