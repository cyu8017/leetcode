// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

using System;

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
    private int leftCount, rightCount;

    public bool BtreeGameWinningMove(TreeNode root, int n, int x) {
        leftCount = rightCount = 0;
        Dfs(root, x);
        return Math.Max(Math.Max(leftCount, rightCount), n - leftCount - rightCount - 1) > n / 2;
    }

    private int Dfs(TreeNode node, int x) {
        if (node == null) return 0;
        int l = Dfs(node.left, x), r = Dfs(node.right, x);
        if (node.val == x) { leftCount = l; rightCount = r; }
        return l + r + 1;
    }
}
