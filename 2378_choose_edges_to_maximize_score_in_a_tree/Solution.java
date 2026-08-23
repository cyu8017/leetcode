// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<int[]>[] g;

    public long maxScore(int[][] edges) {
        int n = edges.length + 1;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            int p = edges[i - 1][0], w = edges[i - 1][1];
            g[p].add(new int[] {i, w});
            g[i].add(new int[] {p, w});
        }
        return dfs(0, -1)[0];
    }

    // returns {withBestEdgeChosenFromChildren, without}
    private long[] dfs(int u, int p) {
        long base = 0;
        long bestGain = 0;
        for (int[] e : g[u]) {
            int to = e[0], w = e[1];
            if (to == p) continue;
            long[] child = dfs(to, u);
            base += child[0];
            long gain = child[1] + w - child[0];
            if (gain > bestGain) bestGain = gain;
        }
        return new long[] {base + bestGain, base};
    }
}
