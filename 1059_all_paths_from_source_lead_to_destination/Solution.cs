// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

using System.Collections.Generic;

public class Solution {
    public bool LeadsToDestination(int n, int[][] edges, int source, int destination) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new List<int>();
        }
        foreach (var e in edges) {
            graph[e[0]].Add(e[1]);
        }
        int[] state = new int[n]; // 0 unvisited, 1 in progress, 2 confirmed

        bool Dfs(int node) {
            if (graph[node].Count == 0) {
                return node == destination;
            }
            if (state[node] == 1) {
                return false;
            }
            if (state[node] == 2) {
                return true;
            }
            state[node] = 1;
            foreach (int nxt in graph[node]) {
                if (!Dfs(nxt)) {
                    return false;
                }
            }
            state[node] = 2;
            return true;
        }

        return Dfs(source);
    }
}
