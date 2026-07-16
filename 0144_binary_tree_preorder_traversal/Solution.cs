// LeetCode 0144 - Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

using System.Collections.Generic;
public class TreeNode { public int val; public TreeNode left; public TreeNode right; public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) { this.val = val; this.left = left; this.right = right; } }
public class Solution {
    public IList<int> PreorderTraversal(TreeNode root) {
        var result = new List<int>();
        Traverse(root, result);
        return result;
    }
    private void Traverse(TreeNode node, IList<int> result) {
        if (node == null) return;
        result.Add(node.val); Traverse(node.left, result); Traverse(node.right, result);
    }
}