// LeetCode 1315 - Sum Of Nodes With Even Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

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
    public int sumEvenGrandparent(TreeNode root) {
        return dfs(root, null, null);
    }

    private int dfs(TreeNode node, TreeNode parent, TreeNode grandparent) {
        if (node == null) return 0;
        int add = (grandparent != null && grandparent.val % 2 == 0) ? node.val : 0;
        return add + dfs(node.left, node, parent) + dfs(node.right, node, parent);
    }
}
