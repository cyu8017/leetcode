// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

using System.Collections.Generic;

public class Solution {
    public long MaximumScoreAfterOperations(int[][] edges, int[] values) {
        int n = values.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        long total = 0;
        foreach (int v in values) total += v;
        long Dfs(int u, int p) {
            long sumKids = 0;
            bool isLeaf = true;
            foreach (int v in g[u]) {
                if (v == p) continue;
                isLeaf = false;
                sumKids += Dfs(v, u);
            }
            if (isLeaf) return values[u];
            return values[u] < sumKids ? values[u] : sumKids;
        }
        return total - Dfs(0, -1);
    }
}
