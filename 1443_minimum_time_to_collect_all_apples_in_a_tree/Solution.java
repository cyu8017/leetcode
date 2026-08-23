// LeetCode 1443 - Minimum Time To Collect All Apples In A Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

import java.util.*;

class Solution {
    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }
        return visit(0, -1, graph, hasApple);
    }

    private int visit(int node, int parent, List<List<Integer>> graph, List<Boolean> hasApple) {
        int cost = 0;
        for (int child : graph.get(node)) {
            if (child == parent) continue;
            int childCost = visit(child, node, graph, hasApple);
            if (childCost > 0 || hasApple.get(child)) cost += childCost + 2;
        }
        return cost;
    }
}
