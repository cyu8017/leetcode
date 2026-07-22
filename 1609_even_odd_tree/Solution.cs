// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

using System.Collections.Generic;

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
    public bool IsEvenOddTree(TreeNode root) {
        var q = new List<TreeNode> { root };
        int level = 0;
        while (q.Count > 0) {
            int prev = level % 2 == 0 ? int.MinValue : int.MaxValue;
            var nxt = new List<TreeNode>();
            foreach (var node in q) {
                if (node.val % 2 == level % 2) return false;
                if (level % 2 == 0 && node.val <= prev) return false;
                if (level % 2 == 1 && node.val >= prev) return false;
                prev = node.val;
                if (node.left != null) nxt.Add(node.left);
                if (node.right != null) nxt.Add(node.right);
            }
            q = nxt;
            level++;
        }
        return true;
    }
}
