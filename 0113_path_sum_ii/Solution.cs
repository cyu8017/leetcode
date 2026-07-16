// LeetCode 0113 - Path Sum II
// https://leetcode.com/problems/path-sum-ii/

using System.Collections.Generic;

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    public IList<IList<int>> PathSum(TreeNode root, int targetSum) {
        var paths = new List<IList<int>>();
        Dfs(root, targetSum, new List<int>(), paths);
        return paths;
    }

    private void Dfs(TreeNode node, int remaining, List<int> path,
                     List<IList<int>> paths) {
        if (node == null) return;
        path.Add(node.val);
        if (node.left == null && node.right == null && node.val == remaining) {
            paths.Add(new List<int>(path));
        } else {
            Dfs(node.left, remaining - node.val, path, paths);
            Dfs(node.right, remaining - node.val, path, paths);
        }
        path.RemoveAt(path.Count - 1);
    }
}