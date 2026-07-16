// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

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
    private int best = 0;

    public int DiameterOfBinaryTree(TreeNode root) {
        Depth(root);
        return best;
    }

    private int Depth(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = Depth(node.left);
        int right = Depth(node.right);
        best = System.Math.Max(best, left + right);
        return 1 + System.Math.Max(left, right);
    }
}
