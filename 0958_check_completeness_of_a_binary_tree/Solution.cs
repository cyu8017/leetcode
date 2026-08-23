// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

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
    public bool IsCompleteTree(TreeNode root) {
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        bool end = false;
        while (q.Count > 0) {
            TreeNode node = q.Dequeue();
            if (node == null) end = true;
            else {
                if (end) return false;
                q.Enqueue(node.left);
                q.Enqueue(node.right);
            }
        }
        return true;
    }
}
