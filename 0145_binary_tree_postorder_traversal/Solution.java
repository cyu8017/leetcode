// LeetCode 0145 - Binary Tree Postorder Traversal
// https://leetcode.com/problems/binary-tree-postorder-traversal/

import java.util.*;
class TreeNode { int val; TreeNode left, right; TreeNode() {} TreeNode(int val) { this.val = val; } TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; } }
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        traverse(root, result);
        return result;
    }
    private void traverse(TreeNode node, List<Integer> result) {
        if (node == null) return;
        traverse(node.left, result); traverse(node.right, result); result.add(node.val);
    }
}