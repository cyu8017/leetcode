// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

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
    public TreeNode IncreasingBST(TreeNode root) {
        TreeNode dummy = new TreeNode(0);
        TreeNode cur = dummy;
        void Inorder(TreeNode node) {
            if (node == null) return;
            Inorder(node.left);
            node.left = null;
            cur.right = node;
            cur = node;
            Inorder(node.right);
        }
        Inorder(root);
        return dummy.right;
    }
}
