// CONFIG class=Solution method=countDominantNodes types=None
// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    int ans = 0;

    int dfs(TreeNode node) {
        if (node == null) return Integer.MIN_VALUE;
        int l = dfs(node.left);
        int r = dfs(node.right);
        int mx = Math.max(Math.max(l, r), node.val);
        if (mx == node.val) ans++;
        return mx;
    }

    public int countDominantNodes(TreeNode root) {
        ans = 0;
        dfs(root);
        return ans;
    }
}
