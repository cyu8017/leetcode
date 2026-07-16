// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

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
    public int CountNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = LeftDepth(root);
        int right = RightDepth(root);
        if (left == right) {
            return (1 << left) - 1;
        }
        return 1 + CountNodes(root.left) + CountNodes(root.right);
    }

    private int LeftDepth(TreeNode node) {
        int depth = 0;
        while (node != null) {
            depth++;
            node = node.left;
        }
        return depth;
    }

    private int RightDepth(TreeNode node) {
        int depth = 0;
        while (node != null) {
            depth++;
            node = node.right;
        }
        return depth;
    }
}
