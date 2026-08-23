// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

class Solution {
    private boolean hasPrev;
    private int prev;
    private int best;

    public int minDiffInBST(TreeNode root) {
        hasPrev = false;
        best = Integer.MAX_VALUE;
        inorder(root);
        return best;
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        if (hasPrev) best = Math.min(best, node.val - prev);
        prev = node.val;
        hasPrev = true;
        inorder(node.right);
    }
}
