// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

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
    public int MinCameraCover(TreeNode root) {
        int cameras = 0;
        int Dfs(TreeNode node) {
            if (node == null) return 1;
            int left = Dfs(node.left);
            int right = Dfs(node.right);
            if (left == 0 || right == 0) {
                cameras++;
                return 2;
            }
            if (left == 2 || right == 2) return 1;
            return 0;
        }
        int rootState = Dfs(root);
        return cameras + (rootState == 0 ? 1 : 0);
    }
}
