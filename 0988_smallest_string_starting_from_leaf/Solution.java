// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

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
    private String best = "~";

    public String smallestFromLeaf(TreeNode root) {
        best = "~";
        dfs(root, "");
        return best;
    }

    private void dfs(TreeNode node, String path) {
        if (node == null) return;
        path = (char) ('a' + node.val) + path;
        if (node.left == null && node.right == null) {
            if (path.compareTo(best) < 0) best = path;
            return;
        }
        dfs(node.left, path);
        dfs(node.right, path);
    }
}
