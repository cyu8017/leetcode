// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    static final int MOD = 1_000_000_007;
    static final int LOG = 17;
    int[] depth;
    int[][] parent;
    List<Integer>[] graph;

    void dfs(int u, int p) {
        parent[0][u] = p;
        for (int v : graph[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
            }
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

    int modPow(int exp) {
        long base = 2, res = 1;
        while (exp > 0) {
            if ((exp & 1) != 0) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return (int) res;
    }

    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        depth = new int[n + 1];
        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new ArrayList<>();
        parent = new int[LOG][n + 1];
        for (int[] row : parent) Arrays.fill(row, -1);
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        dfs(1, -1);
        for (int k = 1; k < LOG; k++)
            for (int v = 1; v <= n; v++)
                if (parent[k - 1][v] != -1) parent[k][v] = parent[k - 1][parent[k - 1][v]];
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) { ans[i] = 0; continue; }
            int a = lca(u, v);
            int d = depth[u] + depth[v] - 2 * depth[a];
            ans[i] = modPow(d - 1);
        }
        return ans;
    }
}
