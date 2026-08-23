// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

using System.Collections.Generic;

public class Solution {
    public int[] MinimumWeight(int[][] edges, int[][] queries) {
        int n = edges.Length + 1;
        var g = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        const int LOG = 17;
        int[][] parent = new int[LOG][];
        for (int k = 0; k < LOG; k++) {
            parent[k] = new int[n];
            for (int v = 0; v < n; v++) parent[k][v] = -1;
        }
        int[] depth = new int[n], dist = new int[n];
        void Dfs(int u, int p) {
            parent[0][u] = p;
            foreach (var (to, w) in g[u]) {
                if (to == p) continue;
                depth[to] = depth[u] + 1;
                dist[to] = dist[u] + w;
                Dfs(to, u);
            }
        }
        Dfs(0, -1);
        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                if (parent[k - 1][v] != -1)
                    parent[k][v] = parent[k - 1][parent[k - 1][v]];
        int Lca(int u, int v) {
            if (depth[u] < depth[v]) { int tmp = u; u = v; v = tmp; }
            for (int k = LOG - 1; k >= 0; k--)
                if (parent[k][u] != -1 && depth[parent[k][u]] >= depth[v])
                    u = parent[k][u];
            if (u == v) return u;
            for (int k = LOG - 1; k >= 0; k--)
                if (parent[k][u] != -1 && parent[k][u] != parent[k][v]) {
                    u = parent[k][u];
                    v = parent[k][v];
                }
            return parent[0][u];
        }
        int Path(int u, int v) {
            int a = Lca(u, v);
            return dist[u] + dist[v] - 2 * dist[a];
        }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int a = queries[i][0], b = queries[i][1], c = queries[i][2];
            ans[i] = (Path(a, b) + Path(b, c) + Path(a, c)) / 2;
        }
        return ans;
    }
}
