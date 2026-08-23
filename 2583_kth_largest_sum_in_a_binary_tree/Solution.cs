// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

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
    public long KthLargestLevelSum(TreeNode root, int k) {
        if (root == null) return -1;
        var sums = new List<long>();
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        while (q.Count > 0) {
            int sz = q.Count;
            long s = 0;
            for (int i = 0; i < sz; ++i) {
                TreeNode node = q.Dequeue();
                s += node.val;
                if (node.left != null) q.Enqueue(node.left);
                if (node.right != null) q.Enqueue(node.right);
            }
            sums.Add(s);
        }
        sums.Sort((a, b) => b.CompareTo(a));
        if (k > sums.Count) return -1;
        return sums[k - 1];
    }
}
