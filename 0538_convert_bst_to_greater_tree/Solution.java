// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

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

public class Solution {
    public void convertBST(TreeNode root) {
        int[] running = new int[] {0};
        reverseInorder(root, running);
    }

    private void reverseInorder(TreeNode node, int[] running) {
        if (node == null) {
            return;
        }
        reverseInorder(node.right, running);
        running[0] += node.val;
        node.val = running[0];
        reverseInorder(node.left, running);
    }
}
