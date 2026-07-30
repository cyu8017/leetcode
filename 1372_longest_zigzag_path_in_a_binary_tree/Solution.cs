// LeetCode 1372 - Longest Zigzag Path In A Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    int ans;
    public int LongestZigZag(TreeNode root) {
        ans = 0; Dfs(root); return ans;
    }
    (int, int) Dfs(TreeNode node) {
        if (node == null) return (-1, -1);
        var l = Dfs(node.left); var r = Dfs(node.right);
        int a = l.Item2 + 1, b = r.Item1 + 1;
        ans = System.Math.Max(ans, System.Math.Max(a, b));
        return (a, b);
    }
}
