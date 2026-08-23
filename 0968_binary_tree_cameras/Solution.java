// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

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
    private int cameras = 0;

    public int minCameraCover(TreeNode root) {
        int rootState = dfs(root);
        return cameras + (rootState == 0 ? 1 : 0);
    }

    // 0 = needs camera, 1 = covered, 2 = has camera
    private int dfs(TreeNode node) {
        if (node == null) return 1;
        int left = dfs(node.left);
        int right = dfs(node.right);
        if (left == 0 || right == 0) {
            cameras++;
            return 2;
        }
        if (left == 2 || right == 2) return 1;
        return 0;
    }
}
