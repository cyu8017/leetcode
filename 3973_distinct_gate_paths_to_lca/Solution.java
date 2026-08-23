// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final long MOD = 1000000007;

    private static long[][] multiply(long[][] a, long[][] b) {
        long[][] c = new long[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return c;
    }

    public int gatePathXor(int n, int[] parent, int[][] gates, int[][] queries) {
        int logn = 1;
        while ((1 << logn) <= n) logn++;
        int[][] up = new int[logn][n];
        long[][][][] product = new long[logn][n][2][2];
        List<Integer>[] children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int node = 1; node < n; node++) children[parent[node]].add(node);
        int[] depth = new int[n];
        List<Integer> order = new ArrayList<>();
        order.add(0);
        for (int i = 0; i < order.size(); i++) {
            int u = order.get(i);
            for (int v : children[u]) {
                depth[v] = depth[u] + 1;
                order.add(v);
            }
        }
        for (int u = 0; u < n; u++) {
            up[0][u] = (u == 0) ? 0 : parent[u];
            product[0][u] = new long[][] {
                { gates[u][1], gates[u][2] },
                { gates[u][2], gates[u][0] }
            };
        }
        for (int level = 1; level < logn; level++) {
            for (int u = 0; u < n; u++) {
                int mid = up[level - 1][u];
                up[level][u] = up[level - 1][mid];
                product[level][u] = multiply(product[level - 1][u], product[level - 1][mid]);
            }
        }
        int answer = 0;
        for (int[] query : queries) {
            int ancestor = lca(query[0], query[2], depth, up, logn);
            long alice = ways(query[0], query[1], depth[query[0]] - depth[ancestor], up, product);
            long bob = ways(query[2], query[3], depth[query[2]] - depth[ancestor], up, product);
            int total = (int) (alice * bob % MOD);
            answer ^= total;
        }
        return answer;
    }

    private int liftNode(int node, int distance, int[][] up) {
        for (int level = 0; distance > 0; level++) {
            if ((distance & 1) != 0) node = up[level][node];
            distance >>= 1;
        }
        return node;
    }

    private int lca(int a, int b, int[] depth, int[][] up, int logn) {
        if (depth[a] > depth[b]) a = liftNode(a, depth[a] - depth[b], up);
        else if (depth[b] > depth[a]) b = liftNode(b, depth[b] - depth[a], up);
        if (a == b) return a;
        for (int level = logn - 1; level >= 0; level--) {
            if (up[level][a] != up[level][b]) {
                a = up[level][a];
                b = up[level][b];
            }
        }
        return up[0][a];
    }

    private long ways(int node, int card, int distance, int[][] up, long[][][][] product) {
        long[] vector = new long[2];
        vector[card] = 1;
        for (int level = 0; distance > 0; level++) {
            if ((distance & 1) != 0) {
                long[][] matrix = product[level][node];
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
}
