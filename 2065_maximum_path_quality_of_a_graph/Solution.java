// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

import java.util.*;

class Solution {
    private List<int[]>[] g;
    private int[] values;
    private int maxTime, ans;
    private int[] vis;

    public int maximalPathQuality(int[] values, int[][] edges, int maxTime) {
        this.values = values;
        this.maxTime = maxTime;
        int n = values.length;
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(new int[] { e[1], e[2] });
            g[e[1]].add(new int[] { e[0], e[2] });
        }
        ans = 0;
        vis = new int[n];
        dfs(0, 0, 0);
        return ans;
    }

    private void dfs(int u, int time, int quality) {
        if (time > maxTime) return;
        boolean first = vis[u] == 0;
        if (first) quality += values[u];
        vis[u]++;
        if (u == 0) ans = Math.max(ans, quality);
        for (int[] e : g[u]) dfs(e[0], time + e[1], quality);
        vis[u]--;
    }
}
