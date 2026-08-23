// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

using System;
using System.Collections.Generic;
using System.Linq;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    public IList<IList<int>> VerticalTraversal(TreeNode root) {
        var nodes = new List<(int col, int row, int val)>();
        void Dfs(TreeNode node, int row, int col) {
            if (node == null) return;
            nodes.Add((col, row, node.val));
            Dfs(node.left, row + 1, col - 1);
            Dfs(node.right, row + 1, col + 1);
        }
        Dfs(root, 0, 0);
        nodes.Sort();
        var byCol = new SortedDictionary<int, List<int>>();
        foreach (var (col, row, val) in nodes) {
            if (!byCol.ContainsKey(col)) byCol[col] = new List<int>();
            byCol[col].Add(val);
        }
        return byCol.Values.Cast<IList<int>>().ToList();
    }
}
