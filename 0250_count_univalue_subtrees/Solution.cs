// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

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
    private int count;

    public int CountUnivalSubtrees(TreeNode root) {
        count = 0;
        Dfs(root);
        return count;
    }

    private bool Dfs(TreeNode node) {
        if (node == null) {
            return true;
        }
        bool leftOk = Dfs(node.left);
        bool rightOk = Dfs(node.right);
        if (!leftOk || !rightOk) {
            return false;
        }
        if (node.left != null && node.left.val != node.val) {
            return false;
        }
        if (node.right != null && node.right.val != node.val) {
            return false;
        }
        count++;
        return true;
    }
}
