// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

import java.util.ArrayDeque;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<Object[]> queue = new ArrayDeque<>();
        queue.offer(new Object[] {root, 0L});
        int best = 0;
        while (!queue.isEmpty()) {
            long left = (Long) queue.peek()[1];
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                Object[] cur = queue.poll();
                TreeNode node = (TreeNode) cur[0];
                long idx = (Long) cur[1];
                best = Math.max(best, (int) (idx - left + 1));
                if (node.left != null) {
                    queue.offer(new Object[] {node.left, idx * 2});
                }
                if (node.right != null) {
                    queue.offer(new Object[] {node.right, idx * 2 + 1});
                }
            }
        }
        return best;
    }
}
