// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

using System;
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
    Dictionary<TreeNode, List<TreeNode>> g = new Dictionary<TreeNode, List<TreeNode>>();
    Dictionary<int, bool> vis = new Dictionary<int, bool>();

    void Dfs(TreeNode node, TreeNode p) {
        if (node == null) return;
        g[node] = new List<TreeNode> { p, node.left, node.right };
        Dfs(node.left, node);
        Dfs(node.right, node);
    }

    int Dfs2(TreeNode node) {
        if (node == null || (vis.ContainsKey(node.val) && vis[node.val])) return 0;
        vis[node.val] = true;
        int res = node.val;
        int best = 0;
        foreach (var nxt in g[node]) {
            best = Math.Max(best, Dfs2(nxt));
        }
        vis[node.val] = false;
        return res + best;
    }

    public int MaxSum(TreeNode root) {
        g.Clear();
        vis.Clear();
        Dfs(root, null);
        int ans = int.MinValue;
        foreach (var node in g.Keys) {
            ans = Math.Max(ans, Dfs2(node));
            vis.Clear();
        }
        return ans;
    }
}
