// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

using System.Collections.Generic;

public class Solution {
    const long MOD = 1000000007;

    static long[][] Multiply(long[][] a, long[][] b) {
        var c = new long[][] { new long[2], new long[2] };
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return c;
    }

    public int GatePathXor(int n, int[] parent, int[][] gates, int[][] queries) {
        int logn = 1;
        while ((1 << logn) <= n) logn++;
        int[][] up = new int[logn][];
        long[][][] product = new long[logn][][];
        for (int i = 0; i < logn; i++) {
            up[i] = new int[n];
            product[i] = new long[n][];
        }
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int node = 1; node < n; node++) children[parent[node]].Add(node);
        int[] depth = new int[n];
        var order = new List<int> { 0 };
        for (int i = 0; i < order.Count; i++) {
            int u = order[i];
            foreach (int v in children[u]) {
                depth[v] = depth[u] + 1;
                order.Add(v);
            }
        }
        for (int u = 0; u < n; u++) {
            up[0][u] = (u == 0) ? 0 : parent[u];
            product[0][u] = new long[][] {
                new long[] { gates[u][1], gates[u][2] },
                new long[] { gates[u][2], gates[u][0] }
            };
        }
        for (int level = 1; level < logn; level++) {
            for (int u = 0; u < n; u++) {
                int mid = up[level - 1][u];
                up[level][u] = up[level - 1][mid];
                product[level][u] = Multiply(product[level - 1][u], product[level - 1][mid]);
            }
        }
        int LiftNode(int node, int distance) {
            for (int level = 0; distance > 0; level++) {
                if ((distance & 1) != 0) node = up[level][node];
                distance >>= 1;
            }
            return node;
        }
        int Lca(int a, int b) {
            if (depth[a] > depth[b]) a = LiftNode(a, depth[a] - depth[b]);
            else if (depth[b] > depth[a]) b = LiftNode(b, depth[b] - depth[a]);
            if (a == b) return a;
            for (int level = logn - 1; level >= 0; level--) {
                if (up[level][a] != up[level][b]) {
                    a = up[level][a];
                    b = up[level][b];
                }
            }
            return up[0][a];
        }
        long Ways(int node, int card, int distance) {
            long[] vector = new long[2];
            vector[card] = 1;
            for (int level = 0; distance > 0; level++) {
                if ((distance & 1) != 0) {
                    var matrix = product[level][node];
                    vector = new long[] {
                        (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                        (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD
                    };
                    node = up[level][node];
                }
                distance >>= 1;
            }
            return (vector[0] + vector[1]) % MOD;
        }
        int answer = 0;
        foreach (var query in queries) {
            int ancestor = Lca(query[0], query[2]);
            long alice = Ways(query[0], query[1], depth[query[0]] - depth[ancestor]);
            long bob = Ways(query[2], query[3], depth[query[2]] - depth[ancestor]);
            int total = (int)(alice * bob % MOD);
            answer ^= total;
        }
        return answer;
    }
}
