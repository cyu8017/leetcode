// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

using System;

public class Solution {
    private bool hasPrev;
    private int prev;
    private int best;

    public int MinDiffInBST(TreeNode root) {
        hasPrev = false;
        best = int.MaxValue;
        Inorder(root);
        return best;
    }

    private void Inorder(TreeNode node) {
        if (node == null) return;
        Inorder(node.left);
        if (hasPrev) best = Math.Min(best, node.val - prev);
        prev = node.val;
        hasPrev = true;
        Inorder(node.right);
    }
}
