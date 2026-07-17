// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int findDistance(TreeNode root, int p, int q) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        dfs(root, null, graph);
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] { p, 0 });
        Set<Integer> seen = new HashSet<>();
        seen.add(p);
        while (!queue.isEmpty()) {
            int[] entry = queue.poll();
            int node = entry[0];
            int dist = entry[1];
            if (node == q) {
                return dist;
            }
            for (int nei : graph.get(node)) {
                if (seen.add(nei)) {
                    queue.offer(new int[] { nei, dist + 1 });
                }
            }
        }
        return -1;
    }

    private void dfs(TreeNode node, TreeNode parent, Map<Integer, List<Integer>> graph) {
        if (node == null) {
            return;
        }
        graph.computeIfAbsent(node.val, key -> new ArrayList<>());
        if (parent != null) {
            graph.get(node.val).add(parent.val);
            graph.get(parent.val).add(node.val);
        }
        dfs(node.left, node, graph);
        dfs(node.right, node, graph);
    }
}
