// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

using System;

public class Solution {
    public int MinimumFlips(TreeNode root, bool result) {
        (int f, int t) Dfs(TreeNode node) {
            if (node.left == null && node.right == null)
                return node.val == 0 ? (0, 1) : (1, 0);
            if (node.val == 5) {
                var (f, t) = Dfs(node.left);
                return (t, f);
            }
            var (lf, lt) = Dfs(node.left);
            var (rf, rt) = Dfs(node.right);
            if (node.val == 2) return (lf + rf, Math.Min(Math.Min(lt + rt, lt + rf), lf + rt));
            if (node.val == 3) return (Math.Min(Math.Min(lf + rf, lf + rt), lt + rf), lt + rt);
            if (node.val == 4) return (Math.Min(lf + rf, lt + rt), Math.Min(lf + rt, lt + rf));
            return (0, 0);
        }
        var res = Dfs(root);
        return result ? res.t : res.f;
    }
}

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
