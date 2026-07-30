// LeetCode 1382 - Balance A Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

using System.Collections.Generic;
public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    public TreeNode BalanceBST(TreeNode root) {
        var nodes = new List<TreeNode>();
        void Walk(TreeNode x) { if (x == null) return; Walk(x.left); nodes.Add(x); Walk(x.right); }
        Walk(root);
        TreeNode Build(int l, int r) {
            if (l >= r) return null;
            int m = (l + r) / 2;
            var x = nodes[m];
            x.left = Build(l, m); x.right = Build(m + 1, r);
            return x;
        }
        return Build(0, nodes.Count);
    }
}
