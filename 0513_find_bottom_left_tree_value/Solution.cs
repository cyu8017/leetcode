// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

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
    public int FindBottomLeftValue(TreeNode root) {
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        int leftmost = root.val;
        while (queue.Count > 0) {
            int levelSize = queue.Count;
            for (int index = 0; index < levelSize; index++) {
                TreeNode node = queue.Dequeue();
                if (index == 0) {
                    leftmost = node.val;
                }
                if (node.left != null) {
                    queue.Enqueue(node.left);
                }
                if (node.right != null) {
                    queue.Enqueue(node.right);
                }
            }
        }
        return leftmost;
    }
}
