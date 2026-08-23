// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int maxWeight(int n, int[][] edges, int k, int t) {
        @SuppressWarnings("unchecked")
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) graph[e[0]].add(new int[] {e[1], e[2]});
        @SuppressWarnings("unchecked")
        Set<Integer>[][] dp = new HashSet[n][k + 1];
        for (int u = 0; u < n; u++) {
            for (int i = 0; i <= k; i++) dp[u][i] = new HashSet<>();
            dp[u][0].add(0);
        }
        for (int i = 0; i < k; i++) {
            for (int u = 0; u < n; u++) {
                for (int sum : dp[u][i]) {
                    for (int[] e : graph[u]) {
                        int ns = sum + e[1];
                        if (ns < t) dp[e[0]][i + 1].add(ns);
                    }
                }
            }
        }
        int ans = -1;
        for (int u = 0; u < n; u++)
            for (int sum : dp[u][k]) if (sum > ans) ans = sum;
        return ans;
    }
}
