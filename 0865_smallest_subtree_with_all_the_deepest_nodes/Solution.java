// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

class Solution {
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        return dfs(root).node;
    }

    private Result dfs(TreeNode node) {
        if (node == null) return new Result(0, null);
        Result left = dfs(node.left);
        Result right = dfs(node.right);
        if (left.depth > right.depth) return new Result(left.depth + 1, left.node);
        if (right.depth > left.depth) return new Result(right.depth + 1, right.node);
        return new Result(left.depth + 1, node);
    }

    private static class Result {
        int depth;
        TreeNode node;
        Result(int depth, TreeNode node) {
            this.depth = depth;
            this.node = node;
        }
    }
}
