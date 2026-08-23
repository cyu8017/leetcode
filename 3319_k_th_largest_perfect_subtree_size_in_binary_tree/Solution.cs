// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

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
    public int KthLargestPerfectSubtree(TreeNode root, int k) {
        var sizes = new List<int>();
        (int h, int sz, bool perf) Dfs(TreeNode node) {
            if (node == null) return (0, 0, true);
            var L = Dfs(node.left);
            var R = Dfs(node.right);
            int sz = L.sz + R.sz + 1;
            bool perf = L.perf && R.perf && L.h == R.h;
            if (perf) sizes.Add(sz);
            return (Math.Max(L.h, R.h) + 1, sz, perf);
        }
        Dfs(root);
        sizes.Sort((a, b) => b.CompareTo(a));
        if (k > sizes.Count) return -1;
        return sizes[k - 1];
    }
}
