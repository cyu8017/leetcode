// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

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
    private readonly Dictionary<string, int> counts = new();
    private readonly List<TreeNode> result = new();

    public IList<TreeNode> FindDuplicateSubtrees(TreeNode root) {
        counts.Clear();
        result.Clear();
        Serialize(root);
        return result;
    }

    private string Serialize(TreeNode node) {
        if (node == null) return "#";
        string key = node.val + "," + Serialize(node.left) + "," + Serialize(node.right);
        counts.TryGetValue(key, out int c);
        counts[key] = ++c;
        if (c == 2) result.Add(node);
        return key;
    }
}
