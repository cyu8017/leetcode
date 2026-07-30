// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    int ans;

    public int EqualToDescendants(TreeNode root) {
        ans = 0;
        Dfs(root);
        return ans;
    }

    long Dfs(TreeNode node) {
        if (node == null) return 0;
        long total = Dfs(node.left) + Dfs(node.right);
        if (total == node.val) ans++;
        return total + node.val;
    }
}