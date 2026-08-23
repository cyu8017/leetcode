// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

class Solution {
    private Map<Integer, List<Integer>> g = new HashMap<>();

    public int amountOfTime(TreeNode root, int start) {
        build(root, null);
        int ans = 0;
        Set<Integer> vis = new HashSet<>();
        vis.add(start);
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {start, 0});
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            ans = Math.max(ans, cur[1]);
            for (int nxt : g.getOrDefault(cur[0], List.of())) {
                if (vis.add(nxt)) q.offer(new int[] {nxt, cur[1] + 1});
            }
        }
        return ans;
    }

    private void build(TreeNode node, TreeNode parent) {
        if (node == null) return;
        if (parent != null) {
            g.computeIfAbsent(node.val, k -> new ArrayList<>()).add(parent.val);
            g.computeIfAbsent(parent.val, k -> new ArrayList<>()).add(node.val);
        }
        build(node.left, node);
        build(node.right, node);
    }
}

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
