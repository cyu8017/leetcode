// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

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
    private int val_;
    private int depth_;

    public TreeNode AddOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) return new TreeNode(val, root, null);
        val_ = val;
        depth_ = depth;
        Dfs(root, 1);
        return root;
    }

    private void Dfs(TreeNode node, int current) {
        if (node == null) return;
        if (current == depth_ - 1) {
            node.left = new TreeNode(val_, node.left, null);
            node.right = new TreeNode(val_, null, node.right);
            return;
        }
        Dfs(node.left, current + 1);
        Dfs(node.right, current + 1);
    }
}
