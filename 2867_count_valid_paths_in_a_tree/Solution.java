// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private boolean[] isPrime;
    private List<Integer>[] g;

    public long countPaths(int n, int[][] edges) {
        isPrime = new boolean[n + 1];
        for (int i = 0; i <= n; i++) isPrime[i] = true;
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) isPrime[j] = false;
            }
        }
        g = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        long ans = 0;
        for (int u = 1; u <= n; u++) {
            if (!isPrime[u]) continue;
            long total = 0;
            for (int v : g[u]) {
                int c = dfs(v, u);
                ans += c;
                ans += total * c;
                total += c;
            }
        }
        return ans;
    }

    private int dfs(int u, int p) {
        if (isPrime[u]) return 0;
        int sz = 1;
        for (int v : g[u]) if (v != p) sz += dfs(v, u);
        return sz;
    }
}
