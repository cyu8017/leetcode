// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

using System.Collections.Generic;

public class Solution {
    public long CountPairs(int n, int[][] edges) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) { g[e[0]].Add(e[1]); g[e[1]].Add(e[0]); }
        bool[] vis = new bool[n];
        int Dfs(int u) {
            vis[u] = true;
            int size = 1;
            foreach (int v in g[u]) if (!vis[v]) size += Dfs(v);
            return size;
        }
        long ans = 0, seen = 0;
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) {
                long sz = Dfs(i);
                ans += sz * seen;
                seen += sz;
            }
        }
        return ans;
    }
}
