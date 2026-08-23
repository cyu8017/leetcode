// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] cost;
    private long[] ans;

    private List<Integer> dfs(int u, int p) {
        List<Integer> vals = new ArrayList<>();
        vals.add(cost[u]);
        for (int v : g[u]) {
            if (v == p) continue;
            vals.addAll(dfs(v, u));
        }
        Collections.sort(vals);
        if (vals.size() < 3) {
            ans[u] = 1;
        } else {
            int m = vals.size();
            long cand1 = (long) vals.get(m - 1) * vals.get(m - 2) * vals.get(m - 3);
            long cand2 = (long) vals.get(0) * vals.get(1) * vals.get(m - 1);
            long best = Math.max(cand1, cand2);
            if (best < 0) best = 0;
            ans[u] = best;
        }
        if (vals.size() <= 5) return vals;
        List<Integer> keep = new ArrayList<>();
        keep.add(vals.get(0));
        keep.add(vals.get(1));
        keep.add(vals.get(vals.size() - 3));
        keep.add(vals.get(vals.size() - 2));
        keep.add(vals.get(vals.size() - 1));
        return keep;
    }

    public long[] placedCoins(int[][] edges, int[] cost) {
        int n = cost.length;
        @SuppressWarnings("unchecked")
        List<Integer>[] gg = new ArrayList[n];
        for (int i = 0; i < n; i++) gg[i] = new ArrayList<>();
        for (int[] e : edges) {
            gg[e[0]].add(e[1]);
            gg[e[1]].add(e[0]);
        }
        this.g = gg;
        this.cost = cost;
        this.ans = new long[n];
        dfs(0, -1);
        return ans;
    }
}
