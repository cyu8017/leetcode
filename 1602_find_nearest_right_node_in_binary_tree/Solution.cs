// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

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
    public TreeNode FindNearestRightNode(TreeNode root, TreeNode u) {
        if (root == null) return null;
        int target = u.val;
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        while (q.Count > 0) {
            int size = q.Count;
            for (int i = 0; i < size; i++) {
                var node = q.Dequeue();
                if (node.val == target) return i + 1 < size ? q.Peek() : null;
                if (node.left != null) q.Enqueue(node.left);
                if (node.right != null) q.Enqueue(node.right);
            }
        }
        return null;
    }
}
