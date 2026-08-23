// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

using System.Collections.Generic;

public class Solution {
    public long MaxScore(int[][] edges) {
        int n = edges.Length + 1;
        var g = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) g[i] = new List<(int, int)>();
        for (int i = 1; i < n; i++) {
            int p = edges[i - 1][0], w = edges[i - 1][1];
            g[p].Add((i, w));
            g[i].Add((p, w));
        }
        (long withoutPick, long withBase) Dfs(int u, int p) {
            long bas = 0;
            long bestGain = 0;
            foreach (var (to, w) in g[u]) {
                if (to == p) continue;
                var (without, with) = Dfs(to, u);
                bas += without;
                long gain = with + w - without;
                if (gain > bestGain) bestGain = gain;
            }
            return (bas + bestGain, bas);
        }
        return Dfs(0, -1).withoutPick;
    }
}
