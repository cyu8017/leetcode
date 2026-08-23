// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

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
    public void ConvertBST(TreeNode root) {
        int[] running = { 0 };
        ReverseInorder(root, running);
    }

    private static void ReverseInorder(TreeNode node, int[] running) {
        if (node == null) {
            return;
        }
        ReverseInorder(node.right, running);
        running[0] += node.val;
        node.val = running[0];
        ReverseInorder(node.left, running);
    }
}
