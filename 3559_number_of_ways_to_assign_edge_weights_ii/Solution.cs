// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

using System.Collections.Generic;

public class Solution {
    public int[] AssignEdgeWeights(int[][] edges, int[][] queries) {
        const int MOD = 1000000007;
        const int LOG = 17;
        int n = edges.Length + 1;
        int[] depth = new int[n + 1];
        var graph = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new List<int>();
        int[][] parent = new int[LOG][];
        for (int k = 0; k < LOG; k++) {
            parent[k] = new int[n + 1];
            for (int v = 0; v <= n; v++) parent[k][v] = -1;
        }
        foreach (var e in edges) {
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        void Dfs(int u, int p) {
            parent[0][u] = p;
            foreach (int v in graph[u]) {
                if (v != p) {
                    depth[v] = depth[u] + 1;
                    Dfs(v, u);
                }
            }
        }
        Dfs(1, -1);
        for (int k = 1; k < LOG; k++) {
            for (int v = 1; v <= n; v++) {
                if (parent[k - 1][v] != -1) parent[k][v] = parent[k - 1][parent[k - 1][v]];
            }
        }
        int Lca(int u, int v) {
            if (depth[u] < depth[v]) { int tmp = u; u = v; v = tmp; }
            for (int k = LOG - 1; k >= 0; k--) {
                if (parent[k][u] != -1 && depth[parent[k][u]] >= depth[v]) u = parent[k][u];
            }
            if (u == v) return u;
            for (int k = LOG - 1; k >= 0; k--) {
                if (parent[k][u] != -1 && parent[k][u] != parent[k][v]) {
                    u = parent[k][u];
                    v = parent[k][v];
                }
            }
            return parent[0][u];
        }
        int ModPow(int exp) {
            long bas = 2, res = 1;
            while (exp > 0) {
                if ((exp & 1) != 0) res = res * bas % MOD;
                bas = bas * bas % MOD;
                exp >>= 1;
            }
            return (int)res;
        }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) { ans[i] = 0; continue; }
            int a = Lca(u, v);
            int d = depth[u] + depth[v] - 2 * depth[a];
            ans[i] = ModPow(d - 1);
        }
        return ans;
    }
}
