// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public IList<int> BoundaryOfBinaryTree(TreeNode root) {
        if (root == null) {
            return new List<int>();
        }
        if (IsLeaf(root)) {
            return new List<int> { root.val };
        }

        List<int> result = new List<int> { root.val };
        result.AddRange(LeftBoundary(root.left));
        result.AddRange(Leaves(root));
        result.AddRange(RightBoundary(root.right));
        return result;
    }

    private bool IsLeaf(TreeNode node) {
        return node != null && node.left == null && node.right == null;
    }

    private IList<int> LeftBoundary(TreeNode node) {
        if (node == null || IsLeaf(node)) {
            return new List<int>();
        }
        List<int> result = new List<int> { node.val };
        if (node.left != null) {
            result.AddRange(LeftBoundary(node.left));
        } else {
            result.AddRange(LeftBoundary(node.right));
        }
        return result;
    }

    private IList<int> RightBoundary(TreeNode node) {
        if (node == null || IsLeaf(node)) {
            return new List<int>();
        }
        List<int> result;
        if (node.right != null) {
            result = new List<int>(RightBoundary(node.right));
        } else {
            result = new List<int>(RightBoundary(node.left));
        }
        result.Add(node.val);
        return result;
    }

    private IList<int> Leaves(TreeNode node) {
        if (node == null) {
            return new List<int>();
        }
        if (IsLeaf(node)) {
            return new List<int> { node.val };
        }
        List<int> result = new List<int>();
        result.AddRange(Leaves(node.left));
        result.AddRange(Leaves(node.right));
        return result;
    }
}
