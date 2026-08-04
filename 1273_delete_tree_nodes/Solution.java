// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

import java.util.*;

class Solution {
    public int deleteTreeNodes(int nodes, int[] parent, int[] value) {
        List<Integer>[] children = new List[nodes];
        for (int i = 0; i < nodes; i++) children[i] = new ArrayList<>();
        for (int node = 1; node < nodes; node++) children[parent[node]].add(node);
        return dfs(0, children, value)[1];
    }

    private int[] dfs(int node, List<Integer>[] children, int[] value) {
        int total = value[node], count = 1;
        for (int child : children[node]) {
            int[] result = dfs(child, children, value);
            total += result[0];
            count += result[1];
        }
        return new int[] {total, total == 0 ? 0 : count};
    }
}
