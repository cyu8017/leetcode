// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

using System;
using System.Collections.Generic;

public class Solution {
    public int AmountOfTime(TreeNode root, int start) {
        var g = new Dictionary<int, List<int>>();
        void Build(TreeNode node, TreeNode parent) {
            if (node == null) return;
            if (!g.ContainsKey(node.val)) g[node.val] = new List<int>();
            if (parent != null) {
                g[node.val].Add(parent.val);
                if (!g.ContainsKey(parent.val)) g[parent.val] = new List<int>();
                g[parent.val].Add(node.val);
            }
            Build(node.left, node);
            Build(node.right, node);
        }
        Build(root, null);
        int ans = 0;
        var vis = new HashSet<int> { start };
        var q = new Queue<(int v, int d)>();
        q.Enqueue((start, 0));
        while (q.Count > 0) {
            var (v, d) = q.Dequeue();
            ans = Math.Max(ans, d);
            if (!g.ContainsKey(v)) continue;
            foreach (int nxt in g[v]) {
                if (vis.Add(nxt)) q.Enqueue((nxt, d + 1));
            }
        }
        return ans;
    }
}

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
