// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

public class RopeTreeNode {
    public int len;
    public char val;
    public RopeTreeNode left;
    public RopeTreeNode right;
    public RopeTreeNode() { }
}

public class Solution {
    public char GetKthCharacter(RopeTreeNode root, int k) {
        char Dfs(RopeTreeNode node, int kk) {
            if (node.left == null && node.right == null) return node.val;
            int leftLen = 0;
            if (node.left != null) leftLen = node.left.len > 0 ? node.left.len : 1;
            if (kk <= leftLen) return Dfs(node.left, kk);
            return Dfs(node.right, kk - leftLen);
        }
        return Dfs(root, k);
    }
}
