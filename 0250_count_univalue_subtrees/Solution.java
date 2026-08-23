// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private int count;

    public int countUnivalSubtrees(TreeNode root) {
        count = 0;
        dfs(root);
        return count;
    }

    private boolean dfs(TreeNode node) {
        if (node == null) {
            return true;
        }
        boolean leftOk = dfs(node.left);
        boolean rightOk = dfs(node.right);
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
