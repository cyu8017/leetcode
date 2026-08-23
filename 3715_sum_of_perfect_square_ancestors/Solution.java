// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private List<Integer>[] graph;
    private int[] ks;
    private Map<Integer, Integer> freq;
    private long ans;

    private int kernel(int x) {
        int res = 1;
        for (int p = 2; p * p <= x; p++) {
            int cnt = 0;
            while (x % p == 0) {
                x /= p;
                cnt++;
            }
            if (cnt % 2 == 1) res *= p;
        }
        if (x > 1) res *= x;
        return res;
    }

    private void dfs(int u, int p) {
        ans += freq.getOrDefault(ks[u], 0);
        freq.merge(ks[u], 1, Integer::sum);
        for (int v : graph[u]) if (v != p) dfs(v, u);
        freq.merge(ks[u], -1, Integer::sum);
    }

    public long sumOfAncestors(int n, int[][] edges, int[] nums) {
        @SuppressWarnings("unchecked")
        List<Integer>[] g = new ArrayList[n];
        graph = g;
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        ks = new int[n];
        for (int i = 0; i < n; i++) ks[i] = kernel(nums[i]);
        freq = new HashMap<>();
        ans = 0;
        dfs(0, -1);
        return ans;
    }
}
