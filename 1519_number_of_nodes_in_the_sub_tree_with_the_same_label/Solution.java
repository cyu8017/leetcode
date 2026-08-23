// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

import java.util.*;

class Solution {
    public int[] countSubTrees(int n, int[][] edges, String labels) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        int[] answer = new int[n];
        dfs(0, -1, graph, labels, answer);
        return answer;
    }

    private int[] dfs(int node, int parent, List<List<Integer>> graph, String labels, int[] answer) {
        int[] counts = new int[26];
        counts[labels.charAt(node) - 'a']++;

        for (int neighbor : graph.get(node)) {
            if (neighbor == parent) {
                continue;
            }
            int[] child = dfs(neighbor, node, graph, labels, answer);
            for (int i = 0; i < 26; i++) {
                counts[i] += child[i];
            }
        }

        answer[node] = counts[labels.charAt(node) - 'a'];
        return counts;
    }
}
