// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

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
    int ans;

    public int equalToDescendants(TreeNode root) {
        ans = 0;
        dfs(root);
        return ans;
    }

    private long dfs(TreeNode node) {
        if (node == null) return 0;
        long total = dfs(node.left) + dfs(node.right);
        if (total == node.val) ans++;
        return total + node.val;
    }
}
