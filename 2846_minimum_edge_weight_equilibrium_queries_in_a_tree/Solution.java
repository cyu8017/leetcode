// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<int[]>[] g;
    private int[][] up;
    private int[] depth;
    private int[][] cnt;
    private static final int LOG = 15;

    public int[] minOperationsQueries(int n, int[][] edges, int[][] queries) {
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[] {e[1], e[2]});
            g[e[1]].add(new int[] {e[0], e[2]});
        }
        up = new int[LOG][n];
        depth = new int[n];
        cnt = new int[n][27];
        dfs(0, 0);
        for (int j = 1; j < LOG; j++)
            for (int i = 0; i < n; i++) up[j][i] = up[j - 1][up[j - 1][i]];
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int a = queries[i][0], b = queries[i][1];
            int c = lca(a, b);
            int total = depth[a] + depth[b] - 2 * depth[c];
            int best = 0;
            for (int w = 1; w <= 26; w++) {
                int f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w];
                best = Math.max(best, f);
            }
            ans[i] = total - best;
        }
        return ans;
    }

    private void dfs(int u, int p) {
        up[0][u] = p;
        for (int[] e : g[u]) {
            int v = e[0], w = e[1];
            if (v == p) continue;
            depth[v] = depth[u] + 1;
            System.arraycopy(cnt[u], 0, cnt[v], 0, 27);
            cnt[v][w]++;
            dfs(v, u);
        }
    }

    private int lca(int a, int b) {
        if (depth[a] < depth[b]) {
            int t = a;
            a = b;
            b = t;
        }
        int diff = depth[a] - depth[b];
        for (int j = 0; j < LOG; j++) if ((diff & (1 << j)) != 0) a = up[j][a];
        if (a == b) return a;
        for (int j = LOG - 1; j >= 0; j--) {
            if (up[j][a] != up[j][b]) {
                a = up[j][a];
                b = up[j][b];
            }
        }
        return up[0][a];
    }
}
