// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

class Solution {
    public TreeNode reverseOddLevels(TreeNode root) {
        if (root != null) dfs(root.left, root.right, 1);
        return root;
    }

    private void dfs(TreeNode a, TreeNode b, int level) {
        if (a == null || b == null) return;
        if (level % 2 == 1) {
            int tmp = a.val;
            a.val = b.val;
            b.val = tmp;
        }
        dfs(a.left, b.right, level + 1);
        dfs(a.right, b.left, level + 1);
    }
}

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
