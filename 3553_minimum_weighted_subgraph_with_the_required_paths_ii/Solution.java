// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    static final int LOG = 17;
    int[][] parent;
    int[] depth, dist;
    List<int[]>[] g;

    void dfs(int u, int p) {
        parent[0][u] = p;
        for (int[] e : g[u]) {
            int to = e[0], w = e[1];
            if (to == p) continue;
            depth[to] = depth[u] + 1;
            dist[to] = dist[u] + w;
            dfs(to, u);
        }
    }

    int lca(int u, int v) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        for (int k = LOG - 1; k >= 0; k--)
            if (parent[k][u] != -1 && depth[parent[k][u]] >= depth[v]) u = parent[k][u];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (parent[k][u] != -1 && parent[k][u] != parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        return parent[0][u];
    }

    int path(int u, int v) {
        int a = lca(u, v);
        return dist[u] + dist[v] - 2 * dist[a];
    }

    public int[] minimumWeight(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[] {e[1], e[2]});
            g[e[1]].add(new int[] {e[0], e[2]});
        }
        parent = new int[LOG][n];
        for (int[] row : parent) Arrays.fill(row, -1);
        depth = new int[n];
        dist = new int[n];
        dfs(0, -1);
        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                if (parent[k - 1][v] != -1) parent[k][v] = parent[k - 1][parent[k - 1][v]];
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int a = queries[i][0], b = queries[i][1], c = queries[i][2];
            ans[i] = (path(a, b) + path(b, c) + path(a, c)) / 2;
        }
        return ans;
    }
}
