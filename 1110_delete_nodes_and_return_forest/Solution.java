// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

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
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        Set<Integer> delete = new HashSet<>();
        for (int x : to_delete) delete.add(x);
        List<TreeNode> forest = new ArrayList<>();
        dfs(root, true, delete, forest);
        return forest;
    }

    private TreeNode dfs(TreeNode node, boolean isRoot, Set<Integer> delete, List<TreeNode> forest) {
        if (node == null) return null;
        boolean removed = delete.contains(node.val);
        if (isRoot && !removed) forest.add(node);
        node.left = dfs(node.left, removed, delete, forest);
        node.right = dfs(node.right, removed, delete, forest);
        return removed ? null : node;
    }
}
