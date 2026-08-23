// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private List<int[]>[] g;
    private int k;

    public long maximizeSumOfWeights(int[][] edges, int k) {
        int n = edges.length + 1;
        this.k = k;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[] {e[1], e[2]});
            g[e[1]].add(new int[] {e[0], e[2]});
        }
        return dfs(0, -1)[1];
    }

    /** returns {with parent edge kept, without} */
    private long[] dfs(int u, int p) {
        long base = 0;
        List<Long> gains = new ArrayList<>();
        for (int[] e : g[u]) {
            int to = e[0], w = e[1];
            if (to == p) continue;
            long[] child = dfs(to, u);
            base += child[1];
            long gain = child[0] + w - child[1];
            if (gain > 0) gains.add(gain);
        }
        gains.sort(Collections.reverseOrder());
        long with = base, without = base;
        for (int i = 0; i < gains.size() && i < k - 1; i++) with += gains.get(i);
        for (int i = 0; i < gains.size() && i < k; i++) without += gains.get(i);
        return new long[] {with, without};
    }
}
