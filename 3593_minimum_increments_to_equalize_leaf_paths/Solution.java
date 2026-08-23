// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

import java.util.ArrayList;
import java.util.List;

class Solution {
    List<Integer>[] graph;
    int[] cost;
    int ans;

    public int minIncrease(int n, int[][] edges, int[] cost) {
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        this.cost = cost;
        ans = 0;
        dfs(0, -1);
        return ans;
    }

    long dfs(int u, int p) {
        if (graph[u].size() == 1 && p != -1) return cost[u];
        List<Long> childVals = new ArrayList<>();
        for (int v : graph[u]) {
            if (v == p) continue;
            childVals.add(dfs(v, u));
        }
        if (childVals.isEmpty()) return cost[u];
        long mx = 0;
        for (long c : childVals) mx = Math.max(mx, c);
        for (long c : childVals) if (c < mx) ans++;
        return mx + cost[u];
    }
}
