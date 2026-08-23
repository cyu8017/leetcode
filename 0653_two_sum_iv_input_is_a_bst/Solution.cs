// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

using System.Collections.Generic;

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
    private readonly HashSet<int> seen = new();
    private int k;

    public bool FindTarget(TreeNode root, int k) {
        seen.Clear();
        this.k = k;
        return Dfs(root);
    }

    private bool Dfs(TreeNode node) {
        if (node == null) return false;
        if (seen.Contains(k - node.val)) return true;
        seen.Add(node.val);
        return Dfs(node.left) || Dfs(node.right);
    }
}
