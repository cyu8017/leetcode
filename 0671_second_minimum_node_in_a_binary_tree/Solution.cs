// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private int ans = -1;
    private int rootVal;

    public int FindSecondMinimumValue(TreeNode root) {
        if (root == null) return -1;
        ans = -1;
        rootVal = root.val;
        Dfs(root);
        return ans;
    }

    private void Dfs(TreeNode node) {
        if (node == null) return;
        if (node.val > rootVal) {
            if (ans == -1 || node.val < ans) ans = node.val;
            return;
        }
        Dfs(node.left);
        Dfs(node.right);
    }
}
