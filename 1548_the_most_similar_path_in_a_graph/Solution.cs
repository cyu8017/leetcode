// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

using System.Collections.Generic;

public class Solution {
    public IList<int> MostSimilar(int n, int[][] roads, string[] names, string[] targetPath) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var r in roads) {
            graph[r[0]].Add(r[1]);
            graph[r[1]].Add(r[0]);
        }
        var costs = new int[n];
        var parents = new int[targetPath.Length, n];
        for (int node = 0; node < n; node++) {
            costs[node] = names[node] != targetPath[0] ? 1 : 0;
            parents[0, node] = -1;
        }
        for (int i = 1; i < targetPath.Length; i++) {
            var nextCosts = new int[n];
            for (int node = 0; node < n; node++) {
                int bestCost = int.MaxValue, bestPrev = -1;
                foreach (int previous in graph[node]) {
                    if (costs[previous] < bestCost) {
                        bestCost = costs[previous];
                        bestPrev = previous;
                    }
                }
                nextCosts[node] = bestCost + (names[node] != targetPath[i] ? 1 : 0);
                parents[i, node] = bestPrev;
            }
            costs = nextCosts;
        }
        int end = 0;
        for (int node = 1; node < n; node++)
            if (costs[node] < costs[end]) end = node;
        var path = new int[targetPath.Length];
        for (int i = targetPath.Length - 1; i >= 0; i--) {
            path[i] = end;
            end = parents[i, end];
        }
        return path;
    }
}
