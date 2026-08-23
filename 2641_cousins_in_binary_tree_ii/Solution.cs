// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

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
    public TreeNode ReplaceValueInTree(TreeNode root) {
        if (root == null) return null;
        root.val = 0;
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        while (q.Count > 0) {
            int sz = q.Count;
            int levelSum = 0;
            var level = new List<TreeNode>();
            for (int i = 0; i < sz; i++) {
                TreeNode node = q.Dequeue();
                level.Add(node);
                if (node.left != null) levelSum += node.left.val;
                if (node.right != null) levelSum += node.right.val;
            }
            foreach (TreeNode node in level) {
                int cousin = levelSum;
                if (node.left != null) cousin -= node.left.val;
                if (node.right != null) cousin -= node.right.val;
                if (node.left != null) {
                    node.left.val = cousin;
                    q.Enqueue(node.left);
                }
                if (node.right != null) {
                    node.right.val = cousin;
                    q.Enqueue(node.right);
                }
            }
        }
        return root;
    }
}
