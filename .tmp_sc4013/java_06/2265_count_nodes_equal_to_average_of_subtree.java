// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

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

    private int[] dfs(TreeNode node) {
        if (node == null) return new int[] { 0, 0 };
        int[] L = dfs(node.left);
        int[] R = dfs(node.right);
        int sum = L[0] + R[0] + node.val;
        int cnt = L[1] + R[1] + 1;
        if (sum / cnt == node.val) ans++;
        return new int[] { sum, cnt };
    }

    public int averageOfSubtree(TreeNode root) {
        ans = 0;
        dfs(root);
        return ans;
    }
}
