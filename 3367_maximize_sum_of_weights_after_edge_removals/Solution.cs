// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

using System.Collections.Generic;

public class Solution {
    public long MaximizeSumOfWeights(int[][] edges, int k) {
        int n = edges.Length + 1;
        var g = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        foreach (var e in edges) {
            g[e[0]].Add((e[1], e[2]));
            g[e[1]].Add((e[0], e[2]));
        }
        (long with, long without) Dfs(int u, int p) {
            long bas = 0;
            var gains = new List<long>();
            foreach (var (to, w) in g[u]) {
                if (to == p) continue;
                var child = Dfs(to, u);
                bas += child.without;
                long gain = child.with + w - child.without;
                if (gain > 0) gains.Add(gain);
            }
            gains.Sort((a, b) => b.CompareTo(a));
            long with = bas, without = bas;
            for (int i = 0; i < gains.Count && i < k - 1; i++) with += gains[i];
            for (int i = 0; i < gains.Count && i < k; i++) without += gains[i];
            return (with, without);
        }
        return Dfs(0, -1).without;
    }
}
