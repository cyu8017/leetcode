// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] g;
    private int[] values;
    private int k;
    private int ans;

    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        this.values = values;
        this.k = k;
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

    private int dfs(int u, int p) {
        int sum = values[u] % k;
        for (int v : g[u]) {
            if (v == p) continue;
            sum = (sum + dfs(v, u)) % k;
        }
        if (sum == 0) ans++;
        return sum;
    }
}
