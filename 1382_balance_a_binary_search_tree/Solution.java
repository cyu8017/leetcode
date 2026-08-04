// LeetCode 1382 - Balance A Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

import java.util.*;

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
    public TreeNode balanceBST(TreeNode root) {
        List<TreeNode> nodes = new ArrayList<>();
        walk(root, nodes);
        return build(nodes, 0, nodes.size());
    }

    private void walk(TreeNode x, List<TreeNode> nodes) {
        if (x == null) return;
        walk(x.left, nodes);
        nodes.add(x);
        walk(x.right, nodes);
    }

    private TreeNode build(List<TreeNode> nodes, int l, int r) {
        if (l >= r) return null;
        int m = (l + r) / 2;
        TreeNode x = nodes.get(m);
        x.left = build(nodes, l, m);
        x.right = build(nodes, m + 1, r);
        return x;
    }
}
