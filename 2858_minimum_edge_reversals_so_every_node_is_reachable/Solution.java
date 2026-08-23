// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<int[]>[] g;
    private int[] ans;

    public int[] minEdgeReversals(int n, int[][] edges) {
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            g[u].add(new int[] {v, 0});
            g[v].add(new int[] {u, 1});
        }
        ans = new int[n];
        dfs1(0, -1);
        dfs2(0, -1);
        return ans;
    }

    private void dfs1(int u, int p) {
        for (int[] e : g[u]) {
            int v = e[0], ww = e[1];
            if (v == p) continue;
            ans[0] += ww;
            dfs1(v, u);
        }
    }

    private void dfs2(int u, int p) {
        for (int[] e : g[u]) {
            int v = e[0], ww = e[1];
            if (v == p) continue;
            if (ww == 0) ans[v] = ans[u] + 1;
            else ans[v] = ans[u] - 1;
            dfs2(v, u);
        }
    }
}
