// LeetCode 1443 - Minimum Time To Collect All Apples In A Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

using System.Collections.Generic;
public class Solution {
    public int MinTime(int n, int[][] edges, IList<bool> hasApple) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) { graph[e[0]].Add(e[1]); graph[e[1]].Add(e[0]); }
        int Visit(int node, int parent) {
            int cost = 0;
            foreach (int child in graph[node]) {
                if (child == parent) continue;
                int childCost = Visit(child, node);
                if (childCost > 0 || hasApple[child]) cost += childCost + 2;
            }
            return cost;
        }
        return Visit(0, -1);
    }
}
