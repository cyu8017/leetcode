// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final int LOG = 17;
    private List<Integer>[] g;
    private int[][] up;
    private int[] depth;

    private void dfs(int u, int p) {
        up[0][u] = p;
        for (int v : g[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
            }
        }
    }

    private int lift(int v, int d) {
        for (int k = 0; k < LOG; k++)
            if (((d >> k) & 1) != 0) v = up[k][v];
        return v;
    }

    private int lca(int a, int b) {
        if (depth[a] < depth[b]) {
            int t = a;
            a = b;
            b = t;
        }
        a = lift(a, depth[a] - depth[b]);
        if (a == b) return a;
        for (int k = LOG - 1; k >= 0; k--) {
            if (up[k][a] != up[k][b]) {
                a = up[k][a];
                b = up[k][b];
            }
        }
        return up[0][a];
    }

    private int dist(int a, int b) {
        int c = lca(a, b);
        return depth[a] + depth[b] - 2 * depth[c];
    }

    public int[] closestNode(int n, int[][] edges, int[][] query) {
        @SuppressWarnings("unchecked")
        List<Integer>[] gg = new ArrayList[n];
        g = gg;
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        up = new int[LOG][n];
        depth = new int[n];
        dfs(0, 0);
        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                up[k][v] = up[k - 1][up[k - 1][v]];
        int[] ans = new int[query.length];
        for (int i = 0; i < query.length; i++) {
            int a = query[i][0], b = query[i][1], x = query[i][2];
            int[] cands = { lca(a, b), lca(a, x), lca(b, x) };
            int best = cands[0], bestD = dist(cands[0], x);
            for (int t = 1; t < 3; t++) {
                int d = dist(cands[t], x);
                if (d < bestD) {
                    bestD = d;
                    best = cands[t];
                }
            }
            ans[i] = best;
        }
        return ans;
    }
}
