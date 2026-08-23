// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

using System.Collections.Generic;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int WidthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        var queue = new Queue<(TreeNode node, ulong idx)>();
        queue.Enqueue((root, 0));
        int best = 0;
        while (queue.Count > 0) {
            ulong left = queue.Peek().idx;
            int size = queue.Count;
            for (int i = 0; i < size; ++i) {
                var (node, idx) = queue.Dequeue();
                int width = (int)(idx - left + 1);
                if (width > best) best = width;
                if (node.left != null) queue.Enqueue((node.left, idx * 2));
                if (node.right != null) queue.Enqueue((node.right, idx * 2 + 1));
            }
        }
        return best;
    }
}
