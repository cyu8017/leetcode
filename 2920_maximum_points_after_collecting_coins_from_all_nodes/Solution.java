// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private List<Integer>[] g;
    private int[] coins;
    private int k;
    private Map<Long, Integer> memo;

    public int maximumPoints(int[][] edges, int[] coins, int k) {
        int n = coins.length;
        this.coins = coins;
        this.k = k;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        memo = new HashMap<>();
        return dfs(0, -1, 0);
    }

    private int dfs(int u, int p, int shifts) {
        if (shifts > 14) shifts = 14;
        long key = (((long) u) << 5) | shifts;
        if (memo.containsKey(key)) return memo.get(key);
        int c = coins[u] >> shifts;
        int opt1 = c - k, opt2 = c / 2;
        for (int v : g[u]) {
            if (v == p) continue;
            opt1 += dfs(v, u, shifts);
            opt2 += dfs(v, u, shifts + 1);
        }
        int best = Math.max(opt1, opt2);
        memo.put(key, best);
        return best;
    }
}
