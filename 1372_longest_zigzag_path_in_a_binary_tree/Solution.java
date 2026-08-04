// LeetCode 1372 - Longest ZigZag Path In A Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

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
    private int ans = 0;

    public int longestZigZag(TreeNode root) {
        dfs(root);
        return ans;
    }

    private int[] dfs(TreeNode node) {
        if (node == null) return new int[]{-1, -1};
        int[] l = dfs(node.left), r = dfs(node.right);
        int a = l[1] + 1, b = r[0] + 1;
        ans = Math.max(ans, Math.max(a, b));
        return new int[]{a, b};
    }
}
