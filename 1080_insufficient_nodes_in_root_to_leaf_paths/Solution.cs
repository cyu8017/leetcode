// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

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
    public TreeNode SufficientSubset(TreeNode root, int limit) {
        TreeNode Dfs(TreeNode node, int pathSum) {
            if (node == null) {
                return null;
            }
            pathSum += node.val;
            if (node.left == null && node.right == null) {
                return pathSum >= limit ? node : null;
            }
            node.left = Dfs(node.left, pathSum);
            node.right = Dfs(node.right, pathSum);
            if (node.left == null && node.right == null) {
                return null;
            }
            return node;
        }

        return Dfs(root, 0);
    }
}
