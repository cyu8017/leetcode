// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    public TreeNode InsertIntoMaxTree(TreeNode root, int val) {
        if (root == null || val > root.val) {
            var node = new TreeNode(val);
            node.left = root;
            return node;
        }
        root.right = InsertIntoMaxTree(root.right, val);
        return root;
    }
}
