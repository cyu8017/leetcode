// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

using System.Collections.Generic;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    public bool IsCousins(TreeNode root, int x, int y) {
        var info = new Dictionary<int, (int depth, TreeNode parent)>();
        void Dfs(TreeNode node, TreeNode parent, int depth) {
            if (node == null) return;
            if (node.val == x || node.val == y) info[node.val] = (depth, parent);
            Dfs(node.left, node, depth + 1);
            Dfs(node.right, node, depth + 1);
        }
        Dfs(root, null, 0);
        return info[x].depth == info[y].depth && info[x].parent != info[y].parent;
    }
}
