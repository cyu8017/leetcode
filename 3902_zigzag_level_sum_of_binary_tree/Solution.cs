// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

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
    public long[] ZigzagLevelSum(TreeNode root) {
        var ans = new List<long>();
        var q = new List<TreeNode> { root };
        bool left = true;
        while (q.Count > 0) {
            var nq = new List<TreeNode>();
            foreach (var node in q) {
                if (node.left != null) nq.Add(node.left);
                if (node.right != null) nq.Add(node.right);
            }
            int m = q.Count;
            long s = 0;
            for (int i = 0; i < m; i++) {
                var node = left ? q[i] : q[m - i - 1];
                var child = left ? node.left : node.right;
                if (child == null) break;
                s += node.val;
            }
            ans.Add(s);
            left = !left;
            q = nq;
        }
        return ans.ToArray();
    }
}
