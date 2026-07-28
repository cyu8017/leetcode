// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

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
    public TreeNode sufficientSubset(TreeNode root, int limit) {
        return dfs(root, 0, limit);
    }

    private TreeNode dfs(TreeNode node, int pathSum, int limit) {
        if (node == null) {
            return null;
        }
        pathSum += node.val;
        if (node.left == null && node.right == null) {
            return pathSum >= limit ? node : null;
        }
        node.left = dfs(node.left, pathSum, limit);
        node.right = dfs(node.right, pathSum, limit);
        if (node.left == null && node.right == null) {
            return null;
        }
        return node;
    }
}
