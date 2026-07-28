// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

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
    public int MaxAncestorDiff(TreeNode root) => Dfs(root, root.val, root.val);

    private int Dfs(TreeNode node, int lo, int hi) {
        if (node == null) return hi - lo;
        lo = Math.Min(lo, node.val);
        hi = Math.Max(hi, node.val);
        return Math.Max(Dfs(node.left, lo, hi), Dfs(node.right, lo, hi));
    }
}
