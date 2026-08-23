// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; this.left = left; this.right = right;
    }
}

class Solution {
    Map<TreeNode, List<TreeNode>> g = new HashMap<>();
    Map<Integer, Boolean> vis = new HashMap<>();

    void dfs(TreeNode node, TreeNode p) {
        if (node == null) return;
        List<TreeNode> nbrs = new ArrayList<>();
        nbrs.add(p);
        nbrs.add(node.left);
        nbrs.add(node.right);
        g.put(node, nbrs);
        dfs(node.left, node);
        dfs(node.right, node);
    }

    int dfs2(TreeNode node) {
        if (node == null || Boolean.TRUE.equals(vis.get(node.val))) return 0;
        vis.put(node.val, true);
        int res = node.val;
        int best = 0;
        for (TreeNode nxt : g.get(node)) best = Math.max(best, dfs2(nxt));
        vis.put(node.val, false);
        return res + best;
    }

    public int maxSum(TreeNode root) {
        g.clear();
        vis.clear();
        dfs(root, null);
        int ans = Integer.MIN_VALUE;
        for (TreeNode node : g.keySet()) {
            ans = Math.max(ans, dfs2(node));
            vis.clear();
        }
        return ans;
    }
}
