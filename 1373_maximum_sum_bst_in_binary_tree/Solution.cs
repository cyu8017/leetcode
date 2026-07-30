// LeetCode 1373 - Maximum Sum Bst In Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    int ans;
    public int MaxSumBST(TreeNode root) {
        ans = 0; Dfs(root); return ans;
    }
    (bool, int, int, int) Dfs(TreeNode node) {
        if (node == null) return (true, int.MaxValue, int.MinValue, 0);
        var L = Dfs(node.left); var R = Dfs(node.right);
        if (L.Item1 && R.Item1 && L.Item3 < node.val && node.val < R.Item2) {
            int s = L.Item4 + R.Item4 + node.val;
            ans = System.Math.Max(ans, s);
            return (true, System.Math.Min(L.Item2, node.val), System.Math.Max(R.Item3, node.val), s);
        }
        return (false, 0, 0, 0);
    }
}
