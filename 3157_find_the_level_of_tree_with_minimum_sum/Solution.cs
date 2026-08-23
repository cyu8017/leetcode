// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

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
    public int MinimumLevel(TreeNode root) {
        var q = new Queue<TreeNode>();
        q.Enqueue(root);
        long s = long.MaxValue;
        int ans = 0;
        for (int level = 1; q.Count > 0; level++) {
            long t = 0;
            int m = q.Count;
            while (m-- > 0) {
                TreeNode node = q.Dequeue();
                t += node.val;
                if (node.left != null) q.Enqueue(node.left);
                if (node.right != null) q.Enqueue(node.right);
            }
            if (s > t) { s = t; ans = level; }
        }
        return ans;
    }
}
