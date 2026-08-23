// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

using System.Collections.Generic;

public class Solution {
    public IList<int> EventualSafeNodes(int[][] graph) {
        int n = graph.Length;
        int[] color = new int[n];
        bool Dfs(int node) {
            if (color[node] != 0) return color[node] == 2;
            color[node] = 1;
            foreach (int nei in graph[node]) if (!Dfs(nei)) return false;
            color[node] = 2;
            return true;
        }
        var ans = new List<int>();
        for (int i = 0; i < n; i++) if (Dfs(i)) ans.Add(i);
        return ans;
    }
}
