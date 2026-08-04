// LeetCode 1373 - Maximum Sum BST In Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

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
    private int ans = 0;

    public int maxSumBST(TreeNode root) {
        dfs(root);
        return ans;
    }

    // [isBST(0/1), min, max, sum]
    private int[] dfs(TreeNode node) {
        if (node == null) return new int[]{1, Integer.MAX_VALUE, Integer.MIN_VALUE, 0};
        int[] L = dfs(node.left), R = dfs(node.right);
        if (L[0] == 1 && R[0] == 1 && L[2] < node.val && node.val < R[1]) {
            int sum = L[3] + R[3] + node.val;
            ans = Math.max(ans, sum);
            return new int[]{1, Math.min(L[1], node.val), Math.max(R[2], node.val), sum};
        }
        return new int[]{0, 0, 0, 0};
    }
}
