// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

using System.Collections.Generic;

public class Solution {
    private List<int>[] g;
    private int n;

    public int MagnificentSets(int n, int[][] edges) {
        this.n = n;
        g = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int[] color = new int[n + 1];
        for (int i = 0; i <= n; i++) color[i] = -1;
        var components = new List<List<int>>();
        for (int i = 1; i <= n; i++) {
            if (color[i] != -1) continue;
            var comp = new List<int>();
            var q = new Queue<int>();
            q.Enqueue(i);
            color[i] = 0;
            bool bipartite = true;
            while (q.Count > 0) {
                int u = q.Dequeue();
                comp.Add(u);
                foreach (int v in g[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] ^ 1;
                        q.Enqueue(v);
                    } else if (color[v] == color[u]) {
                        bipartite = false;
                    }
                }
            }
            if (!bipartite) return -1;
            components.Add(comp);
        }
        int ans = 0;
        foreach (var comp in components) {
            int best = 0;
            foreach (int u in comp) {
                int d = BfsDepth(u);
                if (d > best) best = d;
            }
            ans += best;
        }
        return ans;
    }

    private int BfsDepth(int start) {
        int[] dist = new int[n + 1];
        for (int i = 0; i <= n; i++) dist[i] = -1;
        var q = new Queue<int>();
        q.Enqueue(start);
        dist[start] = 1;
        int best = 1;
        while (q.Count > 0) {
            int u = q.Dequeue();
            if (dist[u] > best) best = dist[u];
            foreach (int v in g[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.Enqueue(v);
                }
            }
        }
        return best;
    }
}
