// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

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
    private readonly List<int> subtreeSums = new();

    public bool CheckEqualTree(TreeNode root) {
        subtreeSums.Clear();
        int total = Dfs(root);
        if (subtreeSums.Count > 0) subtreeSums.RemoveAt(subtreeSums.Count - 1);
        if (total % 2 != 0) return false;
        int half = total / 2;
        foreach (int sum in subtreeSums) if (sum == half) return true;
        return false;
    }

    private int Dfs(TreeNode node) {
        if (node == null) return 0;
        int total = node.val + Dfs(node.left) + Dfs(node.right);
        subtreeSums.Add(total);
        return total;
    }
}
