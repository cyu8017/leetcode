// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
    public TreeNode InsertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        TreeNode node = root;
        while (true) {
            if (val < node.val) {
                if (node.left == null) { node.left = new TreeNode(val); break; }
                node = node.left;
            } else {
                if (node.right == null) { node.right = new TreeNode(val); break; }
                node = node.right;
            }
        }
        return root;
    }
}
