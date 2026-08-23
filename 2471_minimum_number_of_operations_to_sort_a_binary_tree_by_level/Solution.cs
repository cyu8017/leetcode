// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

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
    public int MinimumOperations(TreeNode root) {
        if (root == null) return 0;
        int ans = 0;
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        while (q.Count > 0) {
            int sz = q.Count;
            int[] vals = new int[sz];
            for (int i = 0; i < sz; i++) {
                TreeNode node = q.Dequeue();
                vals[i] = node.val;
                if (node.left != null) q.Enqueue(node.left);
                if (node.right != null) q.Enqueue(node.right);
            }
            int[] sorted = (int[])vals.Clone();
            Array.Sort(sorted);
            var pos = new Dictionary<int, int>();
            for (int i = 0; i < sz; i++) pos[vals[i]] = i;
            for (int i = 0; i < sz; i++) {
                if (vals[i] != sorted[i]) {
                    int j = pos[sorted[i]];
                    (vals[i], vals[j]) = (vals[j], vals[i]);
                    pos[vals[j]] = j;
                    pos[vals[i]] = i;
                    ans++;
                }
            }
        }
        return ans;
    }
}
