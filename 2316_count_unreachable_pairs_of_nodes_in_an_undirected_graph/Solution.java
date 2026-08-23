// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private boolean[] vis;

    public long countPairs(int n, int[][] edges) {
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        vis = new boolean[n];
        long ans = 0, seen = 0;
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) {
                long sz = dfs(i);
                ans += sz * seen;
                seen += sz;
            }
        }
        return ans;
    }

    private int dfs(int u) {
        vis[u] = true;
        int size = 1;
        for (int v : g[u]) if (!vis[v]) size += dfs(v);
        return size;
    }
}
