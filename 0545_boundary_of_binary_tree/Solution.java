// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        if (isLeaf(root)) {
            List<Integer> result = new ArrayList<>();
            result.add(root.val);
            return result;
        }

        List<Integer> result = new ArrayList<>();
        result.add(root.val);
        result.addAll(leftBoundary(root.left));
        result.addAll(leaves(root));
        result.addAll(rightBoundary(root.right));
        return result;
    }

    private boolean isLeaf(TreeNode node) {
        return node != null && node.left == null && node.right == null;
    }

    private List<Integer> leftBoundary(TreeNode node) {
        if (node == null || isLeaf(node)) {
            return new ArrayList<>();
        }
        List<Integer> result = new ArrayList<>();
        result.add(node.val);
        if (node.left != null) {
            result.addAll(leftBoundary(node.left));
        } else {
            result.addAll(leftBoundary(node.right));
        }
        return result;
    }

    private List<Integer> rightBoundary(TreeNode node) {
        if (node == null || isLeaf(node)) {
            return new ArrayList<>();
        }
        List<Integer> result;
        if (node.right != null) {
            result = new ArrayList<>(rightBoundary(node.right));
        } else {
            result = new ArrayList<>(rightBoundary(node.left));
        }
        result.add(node.val);
        return result;
    }

    private List<Integer> leaves(TreeNode node) {
        if (node == null) {
            return new ArrayList<>();
        }
        if (isLeaf(node)) {
            List<Integer> result = new ArrayList<>();
            result.add(node.val);
            return result;
        }
        List<Integer> result = new ArrayList<>();
        result.addAll(leaves(node.left));
        result.addAll(leaves(node.right));
        return result;
    }
}
