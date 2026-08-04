// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

import java.util.*;

class Solution {
    public List<Integer> mostSimilar(int n, int[][] roads, String[] names, String[] targetPath) {
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] r : roads) {
            graph[r[0]].add(r[1]);
            graph[r[1]].add(r[0]);
        }
        int[] costs = new int[n];
        int[][] parents = new int[targetPath.length][n];
        for (int node = 0; node < n; node++) {
            costs[node] = names[node].equals(targetPath[0]) ? 0 : 1;
            parents[0][node] = -1;
        }
        for (int i = 1; i < targetPath.length; i++) {
            int[] nextCosts = new int[n];
            for (int node = 0; node < n; node++) {
                int bestCost = Integer.MAX_VALUE;
                int bestPrev = -1;
                for (int previous : graph[node]) {
                    if (costs[previous] < bestCost) {
                        bestCost = costs[previous];
                        bestPrev = previous;
                    }
                }
                nextCosts[node] = bestCost + (names[node].equals(targetPath[i]) ? 0 : 1);
                parents[i][node] = bestPrev;
            }
            costs = nextCosts;
        }
        int end = 0;
        for (int node = 1; node < n; node++) {
            if (costs[node] < costs[end]) {
                end = node;
            }
        }
        int[] path = new int[targetPath.length];
        for (int i = targetPath.length - 1; i >= 0; i--) {
            path[i] = end;
            end = parents[i][end];
        }
        List<Integer> result = new ArrayList<>();
        for (int v : path) {
            result.add(v);
        }
        return result;
    }
}
