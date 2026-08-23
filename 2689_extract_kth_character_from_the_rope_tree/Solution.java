// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

class RopeTreeNode {
    int len;
    char val;
    RopeTreeNode left;
    RopeTreeNode right;
    RopeTreeNode() {}
}

class Solution {
    public char getKthCharacter(RopeTreeNode root, int k) {
        return dfs(root, k);
    }

    private char dfs(RopeTreeNode node, int kk) {
        if (node.left == null && node.right == null) return node.val;
        int leftLen = 0;
        if (node.left != null) leftLen = node.left.len > 0 ? node.left.len : 1;
        if (kk <= leftLen) return dfs(node.left, kk);
        return dfs(node.right, kk - leftLen);
    }
}
