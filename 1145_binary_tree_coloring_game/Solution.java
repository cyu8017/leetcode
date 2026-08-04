// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

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
    private int left, right;

    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        left = right = 0;
        dfs(root, x);
        return Math.max(Math.max(left, right), n - left - right - 1) > n / 2;
    }

    private int dfs(TreeNode node, int x) {
        if (node == null) return 0;
        int l = dfs(node.left, x), r = dfs(node.right, x);
        if (node.val == x) { left = l; right = r; }
        return l + r + 1;
    }
}
