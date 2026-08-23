// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

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
    private int ans = -1;
    private int rootVal;

    public int findSecondMinimumValue(TreeNode root) {
        if (root == null) {
            return -1;
        }
        ans = -1;
        rootVal = root.val;
        dfs(root);
        return ans;
    }

    private void dfs(TreeNode node) {
        if (node == null) {
            return;
        }
        if (node.val > rootVal) {
            if (ans == -1 || node.val < ans) {
                ans = node.val;
            }
            return;
        }
        dfs(node.left);
        dfs(node.right);
    }
}
