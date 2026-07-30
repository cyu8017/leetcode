// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

using System.Collections.Generic;

public class Solution {
    public int DeleteTreeNodes(int nodes, int[] parent, int[] value) {
        var children = new List<int>[nodes];
        for (int i = 0; i < nodes; i++) children[i] = new List<int>();
        for (int node = 1; node < nodes; node++) children[parent[node]].Add(node);

        (int total, int count) Dfs(int node) {
            int total = value[node], count = 1;
            foreach (int child in children[node]) {
                var (childSum, childCount) = Dfs(child);
                total += childSum;
                count += childCount;
            }
            return (total, total == 0 ? 0 : count);
        }
        return Dfs(0).count;
    }
}
