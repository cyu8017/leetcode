// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] price;
    private long ans;

    public long maxOutput(int n, int[][] edges, int[] price) {
        this.price = price;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        ans = 0;
        dfs(0, -1);
        return ans;
    }

    private long dfs(int u, int p) {
        long maxChild = 0;
        for (int v : g[u]) {
            if (v == p) continue;
            long child = dfs(v, u);
            if (child > maxChild) maxChild = child;
            if (child > ans) ans = child;
        }
        return (long) price[u] + maxChild;
    }
}
