// LeetCode 3772 - Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

using System.Collections.Generic;

public class Solution {
    public int[] MaxSubgraphScore(int n, int[][] edges, int[] good) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = -2;
        parent[0] = -1;
        var order = new List<int> { 0 };
        for (int i = 0; i < order.Count; i++) {
            int u = order[i];
            foreach (int v in g[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.Add(v);
                }
            }
        }
        int[] down = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            down[u] = 2 * good[u] - 1;
            foreach (int v in g[u]) {
                if (parent[v] == u && down[v] > 0) down[u] += down[v];
            }
        }
        int[] ans = (int[])down.Clone();
        foreach (int u in order) {
            foreach (int v in g[u]) {
                if (parent[v] == u) {
                    int outside = ans[u];
                    if (down[v] > 0) outside -= down[v];
                    ans[v] = down[v];
                    if (outside > 0) ans[v] += outside;
                }
            }
        }
        return ans;
    }
}
