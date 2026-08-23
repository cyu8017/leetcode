// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

import java.util.*;

class Solution {
    private List<Integer>[] g;
    private int[] price;
    private int[] cnt;

    public int minimumTotalPrice(int n, int[][] edges, int[] price, int[][] trips) {
        this.price = price;
        g = new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        cnt = new int[n];
        for (int[] t : trips) path(t[0], -1, t[1]);
        int[] res = dfs(0, -1);
        return Math.min(res[0], res[1]);
    }

    private boolean path(int u, int p, int target) {
        if (u == target) {
            cnt[u]++;
            return true;
        }
        for (int v : g[u]) {
            if (v == p) continue;
            if (path(v, u, target)) {
                cnt[u]++;
                return true;
            }
        }
        return false;
    }

    private int[] dfs(int u, int p) {
        int full = price[u] * cnt[u], half = full / 2;
        for (int v : g[u]) {
            if (v == p) continue;
            int[] child = dfs(v, u);
            full += Math.min(child[0], child[1]);
            half += child[0];
        }
        return new int[] {full, half};
    }
}
