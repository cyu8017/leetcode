// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

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
    int ans = 0;

    (int sum, int cnt) Dfs(TreeNode node) {
        if (node == null) return (0, 0);
        var (ls, lc) = Dfs(node.left);
        var (rs, rc) = Dfs(node.right);
        int sum = ls + rs + node.val;
        int cnt = lc + rc + 1;
        if (sum / cnt == node.val) ans++;
        return (sum, cnt);
    }

    public int AverageOfSubtree(TreeNode root) {
        ans = 0;
        Dfs(root);
        return ans;
    }
}
