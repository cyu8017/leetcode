// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

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
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        int bestSum = Integer.MIN_VALUE, bestLevel = 1, level = 1;
        while (!queue.isEmpty()) {
            int total = 0, size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                total += node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            if (total > bestSum) {
                bestSum = total;
                bestLevel = level;
            }
            level++;
        }
        return bestLevel;
    }
}
