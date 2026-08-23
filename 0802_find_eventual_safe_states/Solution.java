// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

import java.util.*;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) if (dfs(graph, color, i)) ans.add(i);
        return ans;
    }

    private boolean dfs(int[][] graph, int[] color, int node) {
        if (color[node] != 0) return color[node] == 2;
        color[node] = 1;
        for (int nei : graph[node]) {
            if (!dfs(graph, color, nei)) return false;
        }
        color[node] = 2;
        return true;
    }
}
