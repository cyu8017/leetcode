// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

using System.Collections.Generic;

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
    public IList<string> BinaryTreePaths(TreeNode root) {
        var result = new List<string>();
        Dfs(root, new List<string>(), result);
        return result;
    }

    private void Dfs(TreeNode node, List<string> path, List<string> result) {
        if (node == null) {
            return;
        }
        path.Add(node.val.ToString());
        if (node.left == null && node.right == null) {
            result.Add(string.Join("->", path));
        } else {
            Dfs(node.left, path, result);
            Dfs(node.right, path, result);
        }
        path.RemoveAt(path.Count - 1);
    }
}
