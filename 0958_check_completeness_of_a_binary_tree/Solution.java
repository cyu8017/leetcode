// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

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
    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        boolean end = false;
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node == null) end = true;
            else {
                if (end) return false;
                q.offer(node.left);
                q.offer(node.right);
            }
        }
        return true;
    }
}
