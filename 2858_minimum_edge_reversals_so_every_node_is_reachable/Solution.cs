// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

using System.Collections.Generic;

public class Solution {
    public int[] MinEdgeReversals(int n, int[][] edges) {
        var g = new List<(int v, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            g[u].Add((v, 0));
            g[v].Add((u, 1));
        }
        int[] ans = new int[n];
        void Dfs1(int u, int p) {
            foreach (var (v, ww) in g[u]) {
                if (v == p) continue;
                ans[0] += ww;
                Dfs1(v, u);
            }
        }
        Dfs1(0, -1);
        void Dfs2(int u, int p) {
            foreach (var (v, ww) in g[u]) {
                if (v == p) continue;
                if (ww == 0) ans[v] = ans[u] + 1;
                else ans[v] = ans[u] - 1;
                Dfs2(v, u);
            }
        }
        Dfs2(0, -1);
        return ans;
    }
}
