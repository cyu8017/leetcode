// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

import java.util.ArrayList;
import java.util.List;

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
    private int ans;
    private int k;

    public int countGreatEnoughNodes(TreeNode root, int k) {
        this.k = k;
        this.ans = 0;
        dfs(root);
        return ans;
    }

    private List<Integer> dfs(TreeNode node) {
        if (node == null) return new ArrayList<>();
        List<Integer> vals = new ArrayList<>();
        vals.add(node.val);
        vals.addAll(dfs(node.left));
        vals.addAll(dfs(node.right));
        int smaller = 0;
        for (int v : vals) if (v < node.val) smaller++;
        if (smaller >= k) ans++;
        return vals;
    }
}
