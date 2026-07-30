// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

using System.Collections.Generic;

public class Solution {
    public int[] CountSubTrees(int n, int[][] edges, string labels) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        int[] answer = new int[n];

        int[] Dfs(int node, int parent) {
            int[] counts = new int[26];
            int index = labels[node] - 'a';
            counts[index] = 1;
            foreach (int neighbor in graph[node]) {
                if (neighbor == parent) continue;
                int[] child = Dfs(neighbor, node);
                for (int i = 0; i < 26; i++) counts[i] += child[i];
            }
            answer[node] = counts[index];
            return counts;
        }

        Dfs(0, -1);
        return answer;
    }
}
