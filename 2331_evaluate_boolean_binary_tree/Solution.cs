// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

public class Solution {
    public bool EvaluateTree(TreeNode root) {
        if (root.left == null && root.right == null) return root.val == 1;
        bool l = EvaluateTree(root.left);
        bool r = EvaluateTree(root.right);
        if (root.val == 2) return l || r;
        return l && r;
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
