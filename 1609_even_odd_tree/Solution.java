// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

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
    public boolean isEvenOddTree(TreeNode root) {
        if (root == null) return true;
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        int level = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            int prev = level % 2 == 0 ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (node.val % 2 == level % 2) return false;
                if (level % 2 == 0 && node.val <= prev) return false;
                if (level % 2 == 1 && node.val >= prev) return false;
                prev = node.val;
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            level++;
        }
        return true;
    }
}
