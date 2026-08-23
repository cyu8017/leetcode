// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] values;

    public long maximumScoreAfterOperations(int[][] edges, int[] values) {
        int n = values.length;
        this.values = values;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        long total = 0;
        for (int v : values) total += v;
        return total - dfs(0, -1);
    }

    private long dfs(int u, int p) {
        long sumKids = 0;
        boolean isLeaf = true;
        for (int v : g[u]) {
            if (v == p) continue;
            isLeaf = false;
            sumKids += dfs(v, u);
        }
        if (isLeaf) return values[u];
        return values[u] < sumKids ? values[u] : sumKids;
    }
}
