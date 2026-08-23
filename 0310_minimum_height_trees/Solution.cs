// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

using System.Collections.Generic;

public class Solution {
    public IList<int> FindMinHeightTrees(int n, int[][] edges) {
        if (n <= 2) {
            List<int> small = new();
            for (int node = 0; node < n; node++) {
                small.Add(node);
            }
            return small;
        }

        List<List<int>> graph = new();
        int[] degree = new int[n];
        for (int node = 0; node < n; node++) {
            graph.Add(new List<int>());
        }
        foreach (int[] edge in edges) {
            int left = edge[0];
            int right = edge[1];
            graph[left].Add(right);
            graph[right].Add(left);
            degree[left]++;
            degree[right]++;
        }

        List<int> leaves = new();
        for (int node = 0; node < n; node++) {
            if (degree[node] == 1) {
                leaves.Add(node);
            }
        }

        int remaining = n;
        while (remaining > 2) {
            remaining -= leaves.Count;
            List<int> newLeaves = new();
            foreach (int leaf in leaves) {
                foreach (int neighbor in graph[leaf]) {
                    degree[neighbor]--;
                    if (degree[neighbor] == 1) {
                        newLeaves.Add(neighbor);
                    }
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }
}
