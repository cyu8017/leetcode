// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

public class Solution {
    public TreeNode ReverseOddLevels(TreeNode root) {
        void Dfs(TreeNode a, TreeNode b, int level) {
            if (a == null || b == null) return;
            if (level % 2 == 1) {
                int t = a.val; a.val = b.val; b.val = t;
            }
            Dfs(a.left, b.right, level + 1);
            Dfs(a.right, b.left, level + 1);
        }
        if (root != null) Dfs(root.left, root.right, 1);
        return root;
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
