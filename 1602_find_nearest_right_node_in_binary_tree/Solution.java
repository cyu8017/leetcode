// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

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
    public TreeNode findNearestRightNode(TreeNode root, TreeNode u) {
        if (root == null || u == null) return null;
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (node == u || node.val == u.val) {
                    return i + 1 < size ? q.peek() : null;
                }
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
        }
        return null;
    }
}
