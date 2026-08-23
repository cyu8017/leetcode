// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

import java.util.*;

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
    public int findClosestLeaf(TreeNode root, int k) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Set<Integer> leaves = new HashSet<>();
        build(root, null, graph, leaves);
        Queue<Integer> q = new ArrayDeque<>();
        Set<Integer> seen = new HashSet<>();
        seen.add(k);
        q.offer(k);
        while (!q.isEmpty()) {
            int value = q.poll();
            if (leaves.contains(value)) return value;
            if (!graph.containsKey(value)) continue;
            for (int neighbor : graph.get(value)) {
                if (seen.add(neighbor)) q.offer(neighbor);
            }
        }
        return -1;
    }

    private void build(TreeNode node, TreeNode parent, Map<Integer, List<Integer>> graph, Set<Integer> leaves) {
        if (node == null) return;
        graph.computeIfAbsent(node.val, x -> new ArrayList<>());
        if (parent != null) {
            graph.computeIfAbsent(parent.val, x -> new ArrayList<>());
            graph.get(node.val).add(parent.val);
            graph.get(parent.val).add(node.val);
        }
        if (node.left == null && node.right == null) leaves.add(node.val);
        build(node.right, node, graph, leaves);
        build(node.left, node, graph, leaves);
    }
}
