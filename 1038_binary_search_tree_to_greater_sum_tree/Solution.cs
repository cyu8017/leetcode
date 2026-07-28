// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

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
    private int total;

    public TreeNode BstToGst(TreeNode root) {
        total = 0;
        ReverseInorder(root);
        return root;
    }

    private void ReverseInorder(TreeNode node) {
        if (node == null) return;
        ReverseInorder(node.right);
        total += node.val;
        node.val = total;
        ReverseInorder(node.left);
    }
}
