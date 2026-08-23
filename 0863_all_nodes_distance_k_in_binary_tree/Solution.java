// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

import java.util.*;

class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<TreeNode, List<TreeNode>> graph = new HashMap<>();
        build(root, null, graph);
        Queue<TreeNode> queue = new ArrayDeque<>();
        Set<TreeNode> seen = new HashSet<>();
        queue.offer(target);
        seen.add(target);
        int dist = 0;
        while (!queue.isEmpty()) {
            if (dist == k) {
                List<Integer> ans = new ArrayList<>();
                for (TreeNode node : queue) ans.add(node.val);
                return ans;
            }
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                for (TreeNode nei : graph.getOrDefault(node, Collections.emptyList())) {
                    if (seen.add(nei)) queue.offer(nei);
                }
            }
            dist++;
        }
        return new ArrayList<>();
    }

    private void build(TreeNode node, TreeNode parent, Map<TreeNode, List<TreeNode>> graph) {
        if (node == null) return;
        if (parent != null) {
            graph.computeIfAbsent(node, x -> new ArrayList<>()).add(parent);
            graph.computeIfAbsent(parent, x -> new ArrayList<>()).add(node);
        }
        build(node.left, node, graph);
        build(node.right, node, graph);
    }
}
