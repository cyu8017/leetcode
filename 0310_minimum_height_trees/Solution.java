// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n <= 2) {
            List<Integer> result = new ArrayList<>();
            for (int node = 0; node < n; node++) {
                result.add(node);
            }
            return result;
        }

        List<List<Integer>> graph = new ArrayList<>();
        int[] degree = new int[n];
        for (int node = 0; node < n; node++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int left = edge[0];
            int right = edge[1];
            graph.get(left).add(right);
            graph.get(right).add(left);
            degree[left]++;
            degree[right]++;
        }

        List<Integer> leaves = new ArrayList<>();
        for (int node = 0; node < n; node++) {
            if (degree[node] == 1) {
                leaves.add(node);
            }
        }

        int remaining = n;
        while (remaining > 2) {
            remaining -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();
            for (int leaf : leaves) {
                for (int neighbor : graph.get(leaf)) {
                    degree[neighbor]--;
                    if (degree[neighbor] == 1) {
                        newLeaves.add(neighbor);
                    }
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }
}
