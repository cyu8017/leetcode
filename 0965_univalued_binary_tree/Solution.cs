// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

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
    public bool IsUnivalTree(TreeNode root) {
        if (root == null) return true;
        int v = root.val;
        bool Dfs(TreeNode node) {
            if (node == null) return true;
            if (node.val != v) return false;
            return Dfs(node.left) && Dfs(node.right);
        }
        return Dfs(root);
    }
}
