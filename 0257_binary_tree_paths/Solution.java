// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        dfs(root, new ArrayList<>(), result);
        return result;
    }

    private void dfs(TreeNode node, List<String> path, List<String> result) {
        if (node == null) {
            return;
        }
        path.add(String.valueOf(node.val));
        if (node.left == null && node.right == null) {
            result.add(String.join("->", path));
        } else {
            dfs(node.left, path, result);
            dfs(node.right, path, result);
        }
        path.remove(path.size() - 1);
    }
}
