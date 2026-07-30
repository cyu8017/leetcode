// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

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
    public int MaxLevelSum(TreeNode root) {
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        int bestSum = int.MinValue, bestLevel = 1, level = 1;
        while (q.Count > 0) {
            int total = 0, sz = q.Count;
            for (int i = 0; i < sz; i++) {
                TreeNode node = q.Dequeue();
                total += node.val;
                if (node.left != null) q.Enqueue(node.left);
                if (node.right != null) q.Enqueue(node.right);
            }
            if (total > bestSum) { bestSum = total; bestLevel = level; }
            level++;
        }
        return bestLevel;
    }
}
