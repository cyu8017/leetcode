// LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

using System.Collections.Generic;

public class Solution {
    public long InteractionCost(int n, int[][] edges, int[] group) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        int[] total = new int[21];
        foreach (int x in group) total[x]++;
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
        int[][] count = new int[n][];
        for (int i = 0; i < n; i++) count[i] = new int[21];
        long ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            count[u][group[u]]++;
            foreach (int v in g[u]) {
                if (parent[v] != u) continue;
                for (int c = 1; c <= 20; c++) {
                    int x = count[v][c];
                    ans += (long)x * (total[c] - x);
                    count[u][c] += x;
                }
            }
        }
        return ans;
    }
}
