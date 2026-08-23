// LeetCode 0113 - Path Sum II
// https://leetcode.com/problems/path-sum-ii/

import java.util.*;

class TreeNode {
    int val; TreeNode left; TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; this.left = left; this.right = right;
    }
}

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> paths = new ArrayList<>();
        dfs(root, targetSum, new ArrayList<>(), paths);
        return paths;
    }

    private void dfs(TreeNode node, int remaining, List<Integer> path,
                     List<List<Integer>> paths) {
        if (node == null) return;
        path.add(node.val);
        if (node.left == null && node.right == null && node.val == remaining) {
            paths.add(new ArrayList<>(path));
        } else {
            dfs(node.left, remaining - node.val, path, paths);
            dfs(node.right, remaining - node.val, path, paths);
        }
        path.remove(path.size() - 1);
    }
}