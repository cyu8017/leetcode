// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

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
    public int minimumLevel(TreeNode root) {
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        long s = Long.MAX_VALUE;
        int ans = 0;
        for (int level = 1; !q.isEmpty(); level++) {
            long t = 0;
            int m = q.size();
            while (m-- > 0) {
                TreeNode node = q.poll();
                t += node.val;
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            if (s > t) {
                s = t;
                ans = level;
            }
        }
        return ans;
    }
}
