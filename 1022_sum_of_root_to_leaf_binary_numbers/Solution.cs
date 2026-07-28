// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

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
    public int SumRootToLeaf(TreeNode root) => Dfs(root, 0);

    private int Dfs(TreeNode node, int value) {
        if (node == null) return 0;
        value = value * 2 + node.val;
        if (node.left == null && node.right == null) return value;
        return Dfs(node.left, value) + Dfs(node.right, value);
    }
}
