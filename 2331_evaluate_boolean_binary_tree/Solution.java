// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

class Solution {
    public boolean evaluateTree(TreeNode root) {
        if (root.left == null && root.right == null) return root.val == 1;
        boolean l = evaluateTree(root.left);
        boolean r = evaluateTree(root.right);
        if (root.val == 2) return l || r;
        return l && r;
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
