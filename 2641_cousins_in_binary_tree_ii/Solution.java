// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

import java.util.*;

class Solution {
    public TreeNode replaceValueInTree(TreeNode root) {
        if (root == null) return null;
        root.val = 0;
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            int levelSum = 0;
            List<TreeNode> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                TreeNode node = q.poll();
                level.add(node);
                if (node.left != null) levelSum += node.left.val;
                if (node.right != null) levelSum += node.right.val;
            }
            for (TreeNode node : level) {
                int cousin = levelSum;
                if (node.left != null) cousin -= node.left.val;
                if (node.right != null) cousin -= node.right.val;
                if (node.left != null) {
                    node.left.val = cousin;
                    q.offer(node.left);
                }
                if (node.right != null) {
                    node.right.val = cousin;
                    q.offer(node.right);
                }
            }
        }
        return root;
    }
}
