// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

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
    public IList<IList<string>> PrintTree(TreeNode root) {
        int h = Height(root);
        int rows = h + 1;
        int cols = (1 << (h + 1)) - 1;
        var res = new List<IList<string>>();
        for (int i = 0; i < rows; ++i) {
            var row = new List<string>();
            for (int j = 0; j < cols; ++j) row.Add("");
            res.Add(row);
        }
        Place(root, 0, (cols - 1) / 2, h, res);
        return res;
    }

    private int Height(TreeNode node) {
        if (node == null) return -1;
        return 1 + System.Math.Max(Height(node.left), Height(node.right));
    }

    private void Place(TreeNode node, int r, int c, int h, IList<IList<string>> res) {
        if (node == null) return;
        res[r][c] = node.val.ToString();
        if (r == h) return;
        int offset = 1 << (h - r - 1);
        Place(node.left, r + 1, c - offset, h, res);
        Place(node.right, r + 1, c + offset, h, res);
    }
}
